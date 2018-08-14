#!/usr/bin/python
try:
    import numpy as np
except:
    exit("This script requires the Python package \'NumPy\'. Please install that and try again.")
try:
    import pandas as pd
except:
    exit("This script requires the Python package \'Pandas\'. Please install that and try again.")
try:
    import matplotlib.pyplot as plt
except:
    exit("This script requires the Python package \'MatPlotLib\'. Please install that and try again.")
try:
    import seaborn as sns
except:
    exit("This script requires the Python package \'Seaborn\'. Please install that and try again.")
try:
    import grass.script as grass
except:
    exit("You must have GRASS GIS installed, and be in a GRASS session to run this script")
if int(grass.version()['version'].split('.')[0]) < 7:
    grass.fatal("You must be in GRASS version 7.0.1 or higher to run this script!")
import tempfile, math

    
################# SET UP THESE VALUES ####################
##########################################################
RunLength = 300 #number of years the simulation ran for
digits = 3 #number of digits that simulation year numbers are padded to
prefix = "120psf"
coor = "727195.790391, 4285699.45461" # location(s) at which to take a virtual sediment core
outprefix = "P2" # A prefix for all output files.
baseinterval = 0.001 # the depth intervals at which to collect proxies (default is 1mm)
dispinterval = 100 # the number of depth intervals to amalgamate as the interval for the plot of proxies at the last year (default is 10cm)
miny = -1.25 # optional minimum y value for the output stratigraphy plot
proxyscale ='linear' # Scale for the x axis of the output proxies plot. 'log' or 'linear'
########
grass.message("Gathering data files...")
mapset = grass.read_command('g.mapset', flags = 'lp').strip('\n')#grab mapset to constrain searches
elevmaps = grass.read_command('g.list', flags='m', type='rast', pattern='*%s*Elevation_Map*' % prefix, separator=',', mapset = mapset).strip().split(',')
depthmaps = grass.read_command('g.list', flags='m', type='rast', pattern='*%s*Soil_Depth_Map*' % prefix, separator=',', mapset = mapset).strip().split(',')  
deltamaps = grass.read_command('g.list', flags='m', type='rast', pattern='*%s*ED_rate*' % prefix, separator=',', mapset = mapset).strip().split(',')  
lcovmaps = grass.read_command('g.list', flags='m', type='rast', pattern='*%s*Landcover_Map*' % prefix, separator=',', mapset = mapset).strip().split(',')
farmingmaps = grass.read_command('g.list', flags='m', type='rast', pattern='*%s*Farming_Impacts_Map*' % prefix, separator=',', mapset = mapset).strip().split(',')
grazingmaps = grass.read_command('g.list', flags='m', type='rast', pattern='*%s*Gazing_Impacts_Map*' % prefix, separator=',', mapset = mapset).strip().split(',')
# we will need the initial landcover map for the charcoal calcualtions.
initlcov = "init_veg@PERMANENT"
basinmap = "TEST_BASIN" # We are just gonna use a single overarching basin map for now.
#############################################################
#############################################################

## PREPARE FOR PROXY MODELING
# generate base flow accumulation and direction maps from the DEMs in the list
#n = 0
#basinmaps = []
#for elev in elevmaps:
#    n += 1
#    grass.run_command("r.watershed", quiet=True, overwrite=True, elevation=elevmaps[0], accumulation="Temporary_flacc", drainage="Temporary_fldr")
#    # delineate the uplope catchment basin
#    basinmap = "Temporary_catchment_basin_%s" % str(n).zfill(4)
#    grass.run_command("r.water.outlet", quiet=True, overwrite=True, input="Temporary_fldr", output=basinmap, coordinates=coor)
#    basinmaps.append(basinmap)

#calculate base areal scalars
reg = grass.region() # grab region info, including nsres and ewres
m2percell = reg['nsres'] * reg['ewres']
cm2percell = reg['nsres'] * reg['ewres'] * 10000
# grab the number of upslope cells in the current basin
upslopecells = float(grass.read_command('r.stats', quiet=True, flags='cn', input=basinmap, nsteps='1').strip('\n').split(' ')[1])
scalar = math.pow((upslopecells * m2percell), -0.01 ) #scales basin average readings to the size of the basin. Accounts for time averaging and loss due to localized up-basin sinks.

#change landcover maps to proxy of phytoliths for grasses and woody vegetation
grass.message('Generating phytolith densities.')
#tphytomaps = []
#sphytomaps = []
gphytomaps = []
wphytomaps = []
avphytos = []
for lcovmap, elevmap, deltamap in zip(lcovmaps, elevmaps, deltamaps):
    #Grasses DATA come from Fredlund and Tieszen 1994 for mixed grassland. Annual production of 2g/m2 of opaline grass phytoliths.
    #Woody phytoliths estimated by assuming woody vegetation produces ~2 orders of magnitude fewer phytoliths than grasses, based on data from Irene
    gphyto = "%s_insitu_grassphytos_%s" % (outprefix,lcovmap.split('_Landcover')[0])
    wphyto = "%s_insitu_woodphytos_%s" % (outprefix,lcovmap.split('_Landcover')[0]) # note for Isaac, I'm not sure what the above line does, so I just repeat it here
    grass.mapcalc("${phytomap} = eval(a=nsres()*ewres()*2, b=graph(${lcovmap}, 0,0.1, 5,1, 50,0.4), a*b)", overwrite = True, quiet = True, phytomap = gphyto, lcovmap = lcovmap) # modify yearly phytolith deposition for pure grassland by the actual landcover mixture (perecntage of grass in succession stage), and then scale to size of raster cel. This map is then g/cell of grass phytos.
    grass.mapcalc("${phytomap} = eval(a=nsres()*ewres()*0.02, b=graph(${lcovmap}, 0,0, 7,0.05, 18,0.33, 35,0.37, 50,1), a*b)", overwrite = True, quiet = True, phytomap = wphyto, lcovmap = lcovmap) # ditto for woody phytoliths
    gphytostats = grass.parse_command('r.univar', flags='g', map=gphyto, zones=basinmap) # grab stats for average phytolith concentration
    wphytostats = grass.parse_command('r.univar', flags='g', map=wphyto, zones=basinmap) # grab stats for average phytolith concentration
    avgphytos.append(float(gphytostats['mean']) * scalar)
    avwphytos.append(float(wphytostats['mean']) * scalar)
    gphytomaps.append(gphyto)
    wphytomaps.append(wphyto)

#change farming map to charcoal map
grass.message("Generating charcoal densities.")
#NOTE: The following has landcover values HARDCODED to Mediterranean values. When reparammeterizing for non-Mediterranean environments, these will need to be recoded.
recodeto = tempfile.NamedTemporaryFile()
# set up loop to create charcoal maps
charcoalmaps = []
averagecharc = []
for n, lcovmap, farmingmap in zip(range(len(lcovmaps)),lcovmaps, farmingmaps):
    charcoalmap = "%s_insitu_charcoal_%s" % (outprefix,lcovmap.split('_Landcover')[0])
    # The code below uses graphing functions in mapcalc to translate veg type into above ground biomass (kg/sq m) and percentage of biomass that becomes charcoal, and then multiplying those two to find amount of charcoal produced (kg/sqm), and converting that into pieces per cell (note these are only for larger macro-charcoal between 400-600um). This last conversion is: (Kg charcoal * %charcoal in large size class * density of charcoal) / ( conversion rate from volume to #spherical particles * conversion from kg to g) .
    if n == 0:
        lc = initlcov #Calculate the standing biomass map (kg/sq m) based on year 0 veg, but year 1 farming
    else:
        lc = lastlcov #Calculate the standing biomass map (kg/sq m) based on last year veg, but this year's farming
    grass.mapcalc("${charcoal}=eval(biomass=graph(${lcov}, 0,0, 7,0.1, 18.5,0.66, 35,0.74, 50,1.95), pcntcharc=graph(${lcov}, 0,0, 5,0.0048, 18.5,0.0101, 50,0.0325), if(isnull(${farmingmap}), 0, ((biomass * pcntcharc * 0.0267 * 0.5) / (0.00011304 * 1000))) )", quiet=True, overwrite=True, lcov=lc, charcoal=charcoalmap, farmingmap=farmingmap)
    lastlcov = lcovmap #save current lcov to use next year
    charcoalmaps.append(charcoalmap) # save name of charcoal map to use later
    charcstats = grass.parse_command('r.univar', flags='g', map=charcoalmap, zones=basinmap)
    averagecharc.append(float(charcstats['mean']) * scalar)
#    if charcstats.has_key('mean'):
#        averagecharc.append(float(charcstats['mean']) * scalar)
#    else: # basin is very small, and/or no upstream charcoal deposits. This would create an empty stats dict, so just use 0 to avoid "KeyError" troubles
#        averagecharc.append(0)
        
    
recodeto.close() # close and delete temporary rules file
#change impact maps to artifact densities
grass.message('Generating artifact densities.')
artifactmaps = []
for farmingmap, grazingmap in zip(farmingmaps, grazingmaps):
    grass.run_command("r.surf.random", quiet=True, overwrite=True, flags='i', max=2, output="Temporary_random_surface")
    artifactmap = "%s_Artifact_densities_%s" % (outprefix,farmingmap.split('_Farming_Impacts_Map')[0])
    grass.mapcalc("${artifactmap}=if(isnull(${farmingmap}) && isnull(${grazingmap}), 0, if(isnull(${grazingmap}), ${randmap}+2, ${randmap}))", overwrite=True, quiet=True, artifactmap=artifactmap, farmingmap=farmingmap, grazingmap=grazingmap, randmap="Temporary_random_surface")
    artifactmaps.append(artifactmap)
#now build a pandas dataframe to hold the yearly information about elevation changes and various proxy information, etc.

#clean up temporary maps
grass.run_command("g.remove", quiet=True, flags='f', type='rast', pattern='Temporary*')

grass.message("Compiling yearly depth changes and raw proxy amounts...")
l = []
for i in range(RunLength):
    elev, delta, gphyto, wphyto, artifacts, charcoal, sdepth = grass.read_command('r.what', map = ",".join((elevmaps[i], deltamaps[i], gphytomaps[i], wphytomaps[i], artifactmaps[i], charcoalmaps[i], depthmaps[i])), separator = ",", coordinates = coor).strip('\n').split(",")[3:10]
    l.append({'Year': i, 'Elevation': float(elev), 'Soildepth': float(sdepth), 'Delta': float(delta), 'InSitu Grass Phytoliths': float(gphyto) / cm2percell, 'InSitu Wood Phytoliths': float(wphyto) / cm2percell, "Scaled Basin-Average Grass Phytoliths": float(avgphytos[i]) / cm2percell, "Scaled Basin-Average Wood Phytoliths": float(avwphytos[i]) / cm2percell, "InSitu Charcoal": float(charcoal) / cm2percell, "Scaled Basin-Average Charcoal":float(averagecharc[i]) / cm2percell, 'Artifacts': int(artifacts) / cm2percell})
layers = pd.DataFrame(l)
initdepth = layers.Soildepth[0]
layers["Cumsum"] = layers.Delta.cumsum()+initdepth #calculate cumulative sum
layers.set_index('Year', inplace = True) # first move the "year" column to be the index (1-RunLength)
layers.T.to_csv("%s_CumED.csv" % outprefix)


#set up new dataframe to contain results and run a loop through the stratagraphic data to make "real" layers 
grass.message("Deriving temporal stratigraphy...")
stratigraphy = pd.DataFrame({y:np.arange(RunLength+1) for y in ["Year"]}) #set up new dataframe to contain results of stratigraphic simulation
stratigraphy.set_index('Year', inplace = True) # first move the "year" column to be the index
stratigraphy["Stratum0"] = initdepth # add a column for the base soil (stratum 0)
for idx, row in layers.iterrows(): # run a loop through the stratagraphic data to make "real" layers 
    if idx == 0: # Set up the pre-run soil-depth
        stratigraphy["Stratum0"][idx:RunLength+1] = initdepth # save current depth at this year for the stratum (and fill forward in time)
        old_delta = 0 # set up "old_delta" variable
        stratum = 0 # set up "stratum" variable
        currentdepth = initdepth
    else:
        currentdepth += row['Delta'] # figure out where the surface is this year
        if row['Delta'] >= 0: # Deposition happened this year...
            if old_delta > 0: # ...and deposition happened last year too.
                stratigraphy["Stratum%s" % stratum][idx:RunLength+1] = currentdepth # continue building current stratum
            else: # ...but erosion happened last year.
                stratum += 1 # make new stratum
                stratigraphy["Stratum%s" % stratum] = 0.0 # add a column for the new stratum
                stratigraphy["Stratum%s" % stratum][idx:RunLength+1] = currentdepth # begin building new stratum
        else: # Erosion happened this year...
            for key in stratigraphy.keys(): #loop through strata
                if stratigraphy[key][idx] > currentdepth: # do we need to erode an old stratum?
                    stratigraphy[key][idx:RunLength+1] = currentdepth #erode!
        old_delta = row["Delta"]

#loop is done, make some figs!

#make stacked bar plot
grass.message("Making temporal stratigraphic plot...")
plt.ioff() # explicitly set interactive plotting off
#set up styles with seaborn
sns.set_style("ticks")
sns.set_context("poster", font_scale = 1.1)
colors = sns.cubehelix_palette(stratum+1, start=.75, rot=1.5, dark=.25)
fig, ax = plt.subplots(figsize=(17, 8)) #make blank plot, and set x and y axis limits to the maximum values in the stratigraphy array, and set a wide aspect ratio for the plot
ax.set_autoscale_on(False)
### NOTE: We have to "trick" the plot to get it look like values are measured as below surface. We will actually transform the values to be from below the surface after the plot is made....
for strat in reversed(range(stratum+1)):
    ax.bar(range(RunLength+1), stratigraphy.ix[:,strat], width=1, linewidth=0, color=colors[strat], label="Stratum %s" % strat, bottom=0-stratigraphy.ix[:,stratum][RunLength])
ax.plot(layers.Delta.cumsum()+initdepth-stratigraphy.ix[:,stratum][RunLength], color='0.35', drawstyle="steps-post", linestyle='solid', linewidth=1.5) # plot the outline of where the surface has been
ax.plot((0, RunLength+1), (0,0), color='black', linestyle='dashed', linewidth=1.75) # plot a horizontal line for modern day surface
ax.plot((0, RunLength+1), (initdepth-stratigraphy.ix[:,stratum][RunLength],initdepth-stratigraphy.ix[:,stratum][RunLength]), color='0.35', linestyle='dotted', linewidth=1.75) # plot a horizontal line for original surface
ax.text(5, 0.02, "Final Surface", bbox=dict(facecolor='white', alpha=0.25))# add lables for the horizontal lines
ax.text(5, initdepth-stratigraphy.ix[:,stratum][RunLength] + 0.02, "Initial Surface",bbox=dict(facecolor='white', alpha=0.25))
ax.locator_params(nbins = 8)
ax.set_xlim(0,RunLength+1)
ax.set_ylim(miny,np.amax(np.amax(stratigraphy))-stratigraphy.ix[:,stratum][RunLength])
plt.xlabel('Year')
plt.ylabel('Depth below last surface (m)')
ax.legend(loc='center left', bbox_to_anchor=(1.015, 0.5), fontsize='small', frameon='True', shadow='True', fancybox='True')
fig.subplots_adjust(left=0.065, right=0.90)
sns.despine(fig)
plt.savefig("%s_stratigraphy_stackedbar.png" % outprefix, dpi=300)
plt.close()
mbsstrat = (stratigraphy - stratigraphy.ix[:,stratum][RunLength]) # NOW change the stratigraphy to depth below surface, 
mbsstrat.T.to_csv("%s_stratigraphy.csv" % outprefix) # transpose, and save it out to a file

#loop through the data to make a final proxy count
grass.message("Accumulating proxy-data by depth increments...")
proxylist = [] # set up a list to contain results
for idx, row in layers.iterrows():
    if row['Delta'] > 0: # Deposition occured, so accumulate proxies and depth
        numdepths = int(row['Delta'] / baseinterval) # findout how many depth intervals to add
        for depth in range(numdepths): # now add the correct proportion of proxy to each interval
            proxylist.append([row['InSitu Grass Phytoliths']/numdepths, row['InSitu Wood Phytoliths']/numdepths, row['Scaled Basin-Average Grass Phytoliths']/numdepths, row['Scaled Basin-Average Wood Phytoliths']/numdepths, row['InSitu Charcoal']/numdepths, row['Scaled Basin-Average Charcoal']/numdepths, row['Artifacts']/numdepths])
    elif row['Delta'] < 0: # Erosion occured, so remove proxies and depth
        numdepths = int(row['Delta'] / baseinterval) # findout how many depth intervals to remove
        for depth in range(abs(numdepths)): # now remove the correct number of intervals, including all their proxy data
            try:
                proxylist.pop()
            except(IndexError):
                pass
    else: # no change happened, so pass on by
        pass
for idx, i in enumerate(proxylist):
    i.append((idx+1)*-1*baseinterval) # add cumualtive depth intervals
proxyframe = pd.DataFrame(np.array(proxylist)) # convert to dataframe via np array
labels = ["Grass Phyt, insitu", "Wood Phyt, insitu", "Grass Phyt, bas. av.", "Wood Pht, bas. av.", "Macrocharcoal, insitu", "Macrocharcoal, bas. av.","Artifacts", "Depth"] # create some column labels (will also be used in the plot)
proxyframe.columns = labels # add column labels to proxyframe
proxyframe.to_csv("%s_raw_proxies.csv" % outprefix) # save out the raw proxies dataframe to csv file

grass.message("Creating proxy depth plot...")
accumprox = proxyframe.groupby(np.arange(len(proxyframe))//dispinterval).sum() # aggregate data to the binned display interval (for the plot)
accumprox.drop('Depth', axis=1, inplace=True) # the depth column is now bad due to the summing operation above, remove it
accumprox['Depth'] = np.arange(1,len(accumprox)+1)*(-1*baseinterval*dispinterval)  # Make new depth column with corrected values.
# make a plot of the proxies with depth
deletethis = labels.pop() # just peel off the Depth label so we can use the rest of the labels for the plots.
xlabs = ["g/cc", "g/cc", "pieces/cc", "pieces/cc", "pieces/cc"] # labels for the xaxes in the plot. Need to have same number as there are plots.
sns.set_style("ticks")
sns.set_context("poster", font_scale = 1.1)

fig, axes = plt.subplots(nrows=1, ncols=len(labels), sharey=True, sharex=False, figsize=(18, 8)) #make blank plot, and set size
for color, lab, xlab, ax in zip(sns.cubehelix_palette(len(labels), start=.75, rot=1.5, dark=.25), labels, xlabs, axes):
    ax.barh(accumprox.Depth, accumprox[lab], height=.09, linewidth=1, color=color)
    ax.set_title(lab, loc='left')
    ax.set_xscale(proxyscale)
    ax.set_xlim(xmin=0)
    ax.set_ylim([np.amin(accumprox.Depth), 0])
    ax.set_xlabel(xlab)
    ax.locator_params(axis='x', nbins=3)
    ax.patch.set_visible(False)
    for item in mbsstrat.T[RunLength]:
        ax.axhline(y=item, xmin=0, xmax=1.5, c='0.75', linewidth=1, zorder=0, clip_on=False)
        #ax.plot((0, np.amax(accumprox[lab])), (item,item), color='black', linestyle='dashed', linewidth=1, clip_on=False) # plot a horizontal line for modern day surface
#fig.text(0.5, 0.02, 'Amount of proxy (counts or weights)', ha='center', va='center', fontsize=18)
fig.text(0.04, 0.5, 'Depth Below Surface (m)', ha='center', va='center', rotation='vertical', fontsize=18)
fig.subplots_adjust(bottom=0.11, right=0.95, wspace=0.35)
plt.locator_params(axis = 'y', nbins = len(accumprox))
#plt.locator_params(axis = 'x', nbins = 4)
sns.despine()
plt.savefig("%s_proxies_barplot.png" % outprefix, dpi=300)
plt.close()
accumprox.to_csv("%s_binned_proxies.csv" % outprefix) # save out the binned proxies dataframe to csv file

fig, axes = plt.subplots(nrows=1, ncols=3, sharey=True, sharex=False, figsize=(14, 8)) #make blank plot, and set size
for color, lab, xlab, ax in zip(('yellow','green','blue'), (labels[1],labels[3],labels[4]), (xlabs[1],xlabs[3],xlabs[4]), axes):
    ax.barh(accumprox.Depth, accumprox[lab], height=.09, linewidth=1, color=color)
    ax.set_title(lab, loc='left')
    ax.set_xscale(proxyscale)
    ax.set_xlim(xmin=0)
    ax.set_ylim([np.amin(accumprox.Depth), 0])
    ax.set_xlabel(xlab)
    ax.locator_params(axis='x', nbins=3)
    ax.patch.set_visible(False)
    for item in mbsstrat.T[RunLength]:
        ax.axhline(y=item, xmin=0, xmax=1.5, c='0.75', linewidth=1, zorder=0, clip_on=False)
        #ax.plot((0, np.amax(accumprox[lab])), (item,item), color='black', linestyle='dashed', linewidth=1, clip_on=False) # plot a horizontal line for modern day surface
#fig.text(0.5, 0.02, 'Amount of proxy (counts or weights)', ha='center', va='center', fontsize=18)
fig.text(0.04, 0.5, 'Depth Below Surface (m)', ha='center', va='center', rotation='vertical', fontsize=18)
fig.subplots_adjust(bottom=0.11, right=0.95, wspace=0.35)
plt.locator_params(axis = 'y', nbins = len(accumprox))
#plt.locator_params(axis = 'x', nbins = 4)
sns.despine()
plt.savefig("%s_basav_proxies_barplot.png" % outprefix, dpi=300)
plt.close()
accumprox.to_csv("%s_binned_proxies.csv" % outprefix) # save out the binned proxies dataframe to csv file

grass.message("Finished!")