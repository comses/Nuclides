

# mask to basin
grass.run_command('r.mask', raster = 'basin_mask')


# find cells in basin that eroded in this time step\
r.mapcalc expression=basin_erode = if(Temporary_catchment_basin_0002 == 1 & levol_ED_rate0002 < 0, 1, null())

# note, isaac adds in surface from the entire basin, not just those that erode
# so the question is use the basin_mask as zones, or use basin_erode as zones
erosionstats = grass.parse_command('r.univar', flags='g', map=levol_ED_0001, zones=basin_erode) # grab stats for average phytolith concentration

# Setup parameters
P_0 = 4.49		# production rate of Beryllium-10 in quartz at sea level [at/g/yr] after Stone, 1999.
ltlambda = np.log(2) / 1.5e6 # decay constant
L = 160 	# absorption mean-free path (attentuation length)  [g/cm2]   
p = 2.6 	# density of overburden [ g/cm3]


# calculate topo shielding using r.skyview
r.skyview input=DEM output=shielding ndir=16

for N, z in :
    delta = P_0 * np.exp(-z * L / p) - N * ltlambda
    
    
# example looping apply code
df = pd.DataFrame([np.random.randn(50) for i in range(100)])

# so taking layers from the other script
layers
#add a dummy column for be10
layers['be10'] = 1
layers


proxy_test = []
for idx, row in layers.iterrows():
    numdepths = int(row['Delta'] / baseinterval) # findout how many depth intervals to add
    for depth in range(numdepths): # now add the correct proportion of proxy to each interval
        be_delta = P_0 * np.exp(-z * L / p) - N * ltlambda
        proxy_test.append(be_delta + row['be10'])


proxy_test
