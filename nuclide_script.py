try:
    import grass.script as grass
except:
    exit("You must have GRASS GIS installed, and be in a GRASS session to run this script")
    
import grass.script.array as garray
import numpy as np
import matplotlib.pyplot as plt


coor = '725763.609242,4284801.3547' # "727195.790391, 4285699.45461" # location(s) at which to take a virtual sediment core

grass.run_command('g.region', res = 10)

#get list of elevation maps
elevmaps = grass.read_command('g.list', flags='m', type='rast', pattern='*elevation*', separator=',').strip().split(',')
edmaps = grass.read_command('g.list', flags='m', type='rast', pattern='*ED_rate*', separator=',').strip().split(',')
soildepthmaps = grass.read_command('g.list', flags='m', type='rast', pattern='*soildepth*', separator=',').strip().split(',')


# loop each year of levol output maps
#n = 0
for elev, ed, soildepth in zip(elevmaps, edmaps,soildepthmaps):
    #n += 1
    #calculate drainage direction map
    grass.run_command("r.watershed", quiet=True, overwrite=True, elevation=elev, drainage="fldr_tmp")
    
    # generate basin for sample coordinates
    grass.run_command("r.water.outlet", quiet=True, overwrite=True, input="fldr_tmp", output='basin_tmp', coordinates=coor)
    
    # mask to upstream basin
    grass.run_command('r.mask', raster = 'basin_tmp', overwrite = True)
    
    # find out which cells experienced any erosion
    grass.mapcalc('ED_bin = if('+ ed + ' < 0, 1, null())', overwrite = True)
    
    # update mask to eroded cells
    grass.run_command('r.mask', raster = 'ED_bin', overwrite = True)
    
    # pull the soil depths for the eroded cells in mask
    map = garray.array()
    map.read(soildepth)
    
    #remove mask
    grass.run_command('r.mask', flags = 'r')


np.savetxt("np_map.csv", map, delimiter=",")


#map_int = (map * 100).astype(int)
map_int = (map * 1).astype(int)#.astype(np.object)
print(map_int)


soil_columns = np.empty(map.shape, dtype = np.object)
soil_columns[...] = [[] for _ in len(soil_columns)]



init = 1
for x,y in np.nditer([map_int, None], flags = ['refs_ok']):
    y[...] = [init for i in range(x)]
    #y = [init for i in range(x)]


soil_columns[600,200]

plt.imshow(map)
 
grass.run_command('r.series', input = edbinmaps, output = 'ED_sum', method = 'sum', overwrite = True)


#generate base flow accumulation and direction maps from the DEMs in the list
n = 0
basinmaps = []
for elev in elevmaps:
    n += 1
    grass.run_command("r.watershed", quiet=True, overwrite=True, elevation=elev, drainage="Temporary_fldr")
    # delineate the upslope catchment basin
    basinmap = "Temporary_catchment_basin_%s" % str(n).zfill(4)
    grass.run_command("r.water.outlet", quiet=True, overwrite=True, input="Temporary_fldr", output=basinmap, coordinates=coor)
    basinmaps.append(basinmap)


# find the lowest and highest elevations thru the simulation, and use to set the upper and lower boundaries of the region
elev_stats = grass.parse_command('r.univar', map = elevmaps, flags = 'g')
#3d region
grass.run_command('g.region', res = 10, res3 = 10, b = np.floor(float(elev_stats['min'])), t = np.ceil(float(elev_stats['max'])), tbres = 1)

# mask to basin
grass.run_command('r.mask', raster = basinmaps[0])

# loop through erosion deposition maps to find cells that experienced ANY erosion throughout the simulation length, use them to compute a new mask
#todo


# make two dummy maps
grass.mapcalc('one = 1', overwrite = True)
grass.mapcalc('two = 2', overwrite = True)


# make maps of the minimum and maximum elevations for the entire simulation span
grass.run_command('r.series', input = elevmaps, output = 'min_rast,max_rast', method = 'minimum,maximum', overwrite = True)
grass.mapcalc('min_rast = int(min_rast)', overwrite = True) # floor
grass.mapcalc('max_rast = int(max_rast) + 1', overwrite = True) # ceiling

#make a 3d raster for the max volume to make a mask
grass.run_command('r.to.rast3elev', flags = 'l', input = 'one,two', elevation = 'max_rast,min_rast', output = 'mask_3d', overwrite = True)

# use this coarse resolution layer as a mask
grass.mapcalc3d('vol_mask = if(mask_3d == 1, 1, null())', overwrite = True)

# add the 3d mask
grass.run_command('r3.mask', map = 'vol_mask')

#cleanup maps
grass.run_command('g.remove', flags = 'f', type = 'raster_3d', name = 'mask_3d')                         


# increase the vertical resolution
grass.run_command('g.region', tbres = .01)


# now make high resolution raster mask for the initial elevation surface, masked to 3d mask
grass.mapcalc('init = 1', overwrite=True)
grass.run_command('r.to.rast3elev', flags = 'lm', input = 'init', elevation = elevmaps[0], output = 'vol_test', overwrite = True)
#create a dummy map that has the surface elevation for all cells
grass.run_command('r.to.rast3elev', flags = 'lm', input = elevmaps[0], elevation = elevmaps[0], output = 'elev3d', overwrite = True)
# make a depth map
grass.mapcalc3d('depth3d = elev3d - z()', overwrite = True)

# apply in situ be10 formula
# Setup parameters
P_0 = 4.49		# production rate of Beryllium-10 in quartz at sea level [at/g/yr] after Stone, 1999.
ltlambda = np.log(2) / 1.5e6 # decay constant
L = 160 	# absorption mean-free path (attentuation length)  [g/cm2]   
p = 2.6 	# density of overburden [ g/cm3]

#create a dummy map that has the surface elevation for all cells

expr = 'vol_test2 = ' + str(P_0) + ' * exp( -1 * depth3d * '+ str(L / p) + ') - vol_test * ' + str(ltlambda)
grass.mapcalc3d(expr, overwrite = True)

# now let's try time step 2



# find cells in basin that eroded in this time step\
r.mapcalc expression=basin_erode = if(Temporary_catchment_basin_0002 == 1 & levol_ED_rate0002 < 0, 1, null())

# note, isaac adds in surface from the entire basin, not just those that erode
# so the question is use the basin_mask as zones, or use basin_erode as zones
erosionstats = grass.parse_command('r.univar', flags='g', map=levol_ED_0001, zones=basin_erode) # grab stats for average phytolith concentration




# calculate topo shielding using r.skyview
#r.skyview input=DEM output=shielding ndir=16



