try:
    import grass.script as grass
except:
    exit("You must have GRASS GIS installed, and be in a GRASS session to run this script")


coor = '725763.609242,4284801.3547' # "727195.790391, 4285699.45461" # location(s) at which to take a virtual sediment core

#get list of elevation maps
elevmaps = grass.read_command('g.list', flags='m', type='rast', pattern='*elevation*', separator=',').strip().split(',')


#generate base flow accumulation and direction maps from the DEMs in the list
n = 0
basinmaps = []
for elev in elevmaps:
    n += 1
    grass.run_command("r.watershed", quiet=True, overwrite=True, elevation=elev, drainage="Temporary_fldr")
    # delineate the uplope catchment basin
    basinmap = "Temporary_catchment_basin_%s" % str(n).zfill(4)
    grass.run_command("r.water.outlet", quiet=True, overwrite=True, input="Temporary_fldr", output=basinmap, coordinates=coor)
    basinmaps.append(basinmap)


# find the lowest and highest elevations thru the simulation, and use to set the upper and lower boundaries of the region
elev_stats = grass.parse_command('r.univar', map = elevmaps, flags = 'g')
#3d region
grass.run_command('g.region', res = 10, res3 = 10, b = np.floor(float(elev_stats['min'])), t = np.ceil(float(elev_stats['max'])), tbres = 1)

# mask to basin
grass.run_command('r.mask', raster = basinmaps[0])

# make two dummy maps
grass.mapcalc('one = 1', overwrite = True)
grass.mapcalc('two = 2', overwrite = True)


# make maps of the minimum and maximum elevations for the entire simulation span
grass.run_command('r.series', input = elevmaps, output = 'min_rast,max_rast', method = 'minimum,maximum', overwrite = True)

#make a 3d raster for the max volume to make a mask
grass.run_command('r.to.rast3elev', flags = 'l', input = 'one,two', elevation = 'max_rast,min_rast', output = 'init_3d', overwrite = True)

# use this coarse resolution layer as a mask
grass.mapcalc3d('vol_mask = if(init_3d == 1, 1, null())', overwrite = True)

# add the 3d mask
grass.run_command('r3.mask', map = 'vol_mask')

# increase the vertical resolution
grass.run_command('g.region', tbres = .01)


# now make high resolution raster mask for the initial elevation surface, masked to 3d mask
grass.mapcalc('init = 1', overwrite=True)
grass.run_command('r.to.rast3elev', flags = 'l', input = 'init', elevation = elevmaps[0], output = 'vol_test', overwrite = True)


# apply in situ be10 formula
# Setup parameters
P_0 = 4.49		# production rate of Beryllium-10 in quartz at sea level [at/g/yr] after Stone, 1999.
ltlambda = np.log(2) / 1.5e6 # decay constant
L = 160 	# absorption mean-free path (attentuation length)  [g/cm2]   
p = 2.6 	# density of overburden [ g/cm3]


grass.mapcalc3d(P_0 * np.exp(-z * L / p) - N * ltlambda
str(P_0) + ' * exp(-' + elevmaps[0] + ' - z() * '+ str(L / p) + ') - vol_test * ' + str(ltlambda)

# now let's try time step 2



# find cells in basin that eroded in this time step\
r.mapcalc expression=basin_erode = if(Temporary_catchment_basin_0002 == 1 & levol_ED_rate0002 < 0, 1, null())

# note, isaac adds in surface from the entire basin, not just those that erode
# so the question is use the basin_mask as zones, or use basin_erode as zones
erosionstats = grass.parse_command('r.univar', flags='g', map=levol_ED_0001, zones=basin_erode) # grab stats for average phytolith concentration




# calculate topo shielding using r.skyview
#r.skyview input=DEM output=shielding ndir=16



