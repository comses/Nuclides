import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

########### SET UP VALUES ##################
RunLength = 100 # Number of simulated "years"
initdepth = 1.5 # start with some depth (real script will read in from year 0 soildepth map)
baseinterval = 0.001 # the depth intervals at which to collect proxies (default is 1mm)
dispinterval = 100 # the number of depth intervals to amalgamate as the interval for the plot of proxies at the last year (default is 10cm)
prefix = "test"
############################################

# make some dummy stratigraphic data
di = {k:np.random.normal(0.0075, 0.1, RunLength+1) for k in ["Delta"]} #random normal for elev change
di.update({k:np.random.poisson(5, RunLength+1) for k in ["Proxy1", "Proxy2", "Proxy3", "Proxy4"]}) #random poisson for a variety of proxies in each year
di.update({y:np.arange(RunLength+1) for y in ["Year"]}) # set up column for years (0 to RunLength)
layers = pd.DataFrame(di) # make it into a dataframe
layers['Delta'][0] = 0 #set year 0 to have no change in all the columns
layers['Proxy1'][0] = 0
layers['Proxy2'][0] = 0
layers['Proxy3'][0] = 0
layers['Proxy4'][0] = 0
layers["Cumsum"] = layers.Delta.cumsum()+initdepth # calculate cumulative sum, and put it in a column in
layers.set_index('Year', inplace = True) # move the "Year" column to be the index
layers.T.to_csv("%s_CumED.csv" % prefix) # write out csv for posterity

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
                print "Depositing"
            else: # ...but erosion happened last year.
                stratum += 1 # make new stratum
                stratigraphy["Stratum%s" % stratum] = 0.0 # add a column for the new stratum
                stratigraphy["Stratum%s" % stratum][idx:RunLength+1] = currentdepth # begin building new stratum
                print "New stratum!"
        else: # Erosion happened this year...
            print "Eroding..."
            for key in stratigraphy.keys(): #loop through strata
                if stratigraphy[key][idx] > currentdepth: # do we need to erode an old stratum?
                    stratigraphy[key][idx:RunLength+1] = currentdepth #erode!
        old_delta = row["Delta"]

#stratigraphy loop is done, make the fun temporal stratigraphy plot
### NOTE: We have to "trick" the plot to get it look like values are measured as below surface. We will actually transform the values to be from below the surface at the end of the script....
print "Making temporal stratigraphy plot..."
plt.ioff() # explicitly set interactive plotting off
#set up styles with seaborn
sns.set_style("ticks")
sns.set_context("poster", font_scale = 1.1)
colors = sns.cubehelix_palette(stratum+1, start=.75, rot=1.5, dark=.25)
fig, ax = plt.subplots(figsize=(17, 8)) #make blank plot, and set x and y axis limits to the maximum values in the stratigraphy array, and set a wide aspect ratio for the plot
ax.set_autoscale_on(False)
for strat in reversed(range(stratum+1)):
    ax.bar(range(RunLength+1), stratigraphy.ix[:,strat], width=1, linewidth=0, color=colors[strat], label="Stratum %s" % strat, bottom=0-stratigraphy.ix[:,stratum][RunLength])
ax.plot(layers.Delta.cumsum()+initdepth-stratigraphy.ix[:,stratum][RunLength], color='0.35', drawstyle="steps-post", linestyle='solid', linewidth=1.5) # plot the outline of where the surface has been
ax.plot((0, RunLength+1), (0,0), color='black', linestyle='dashed', linewidth=1.75) # plot a horizontal line for modern day surface
ax.plot((0, RunLength+1), (initdepth-stratigraphy.ix[:,stratum][RunLength],initdepth-stratigraphy.ix[:,stratum][RunLength]), color='0.35', linestyle='dotted', linewidth=1.75) # plot a horizontal line for original surface
ax.text(5, 0.02, "Final Surface", bbox=dict(facecolor='white', alpha=0.25))# add lables for the horizontal lines
ax.text(5, initdepth-stratigraphy.ix[:,stratum][RunLength] + 0.02, "Initial Surface",bbox=dict(facecolor='white', alpha=0.25))
ax.locator_params(nbins = 8)
ax.set_xlim(0,RunLength+1)
ax.set_ylim(0-stratigraphy.ix[:,stratum][RunLength],np.amax(np.amax(stratigraphy))-stratigraphy.ix[:,stratum][RunLength])
plt.xlabel('Year')
plt.ylabel('Depth below last surface (m)')
ax.legend(loc='center left', bbox_to_anchor=(1.015, 0.5), fontsize='small', frameon='True', shadow='True', fancybox='True')
fig.subplots_adjust(left=0.065, right=0.90)
sns.despine(fig)
plt.savefig("%s_stratigraphy_stackedbar.png" % prefix, dpi=300)
plt.close()


        
#loop through the data to make a final proxy count
print "Figuring out the proxies plot"
proxylist = [] # set up a list to contain results
for idx, row in layers.iterrows():
    if row['Delta'] > 0: # Deposition occured, so accumulate proxies and depth
        numdepths = int(row['Delta'] / baseinterval) # findout how many depth intervals to add
        print 'Depositing. %s intervals added' % (numdepths)
        for depth in range(numdepths): # now add the correct proportion of proxy to each interval
            proxylist.append([row['Proxy1']/numdepths,row['Proxy2']/numdepths, row['Proxy3']/numdepths, row['Proxy4']/numdepths])
    elif row['Delta'] < 0: # Erosion occured, so remove proxies and depth
        numdepths = int(row['Delta'] / baseinterval) # findout how many depth intervals to remove
        print 'Eroding. %s intervals removed' % abs(numdepths)
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
proxyframe.columns = ["Proxy1", "Proxy2", "Proxy3", "Proxy4","Depth"] # add column labels

accumprox = proxyframe.groupby(np.arange(len(proxyframe))//dispinterval).sum() # aggregate data to the display interval (for the plot)
accumprox.drop('Depth', axis=1, inplace=True) # the depth column is now bad due to the summing operation above, remove it
accumprox['Depth'] = np.arange(1,len(accumprox)+1)*(-1*baseinterval*dispinterval)  # Make new depth column with corrected values.
# make a plot of the proxies with depth
labels = ["Proxy1", "Proxy2", "Proxy3", "Proxy4"]
sns.set_style("ticks")
sns.set_context("poster", font_scale = 1.1)
fig, axes = plt.subplots(nrows=1, ncols=len(labels), sharey=True, sharex=True, figsize=(12, 8)) #make blank plot, and set size
#axes[0].set_ylim([np.amin(accumprox.Depth), 0])
for color, lab, ax in zip(sns.cubehelix_palette(4, start=.75, rot=1.5, dark=.25), labels, axes):
    ax.barh(accumprox.Depth, accumprox[lab], height=.09, linewidth=1, color=color)
    ax.set_title(lab, loc='left')
    ax.set_xscale('log')
    ax.set_ylim([np.amin(accumprox.Depth), 0])
fig.text(0.5, 0.02, 'Amount of proxy (counts)', ha='center', va='center', fontsize=18)
fig.text(0.04, 0.5, 'Depth Below Surface (m)', ha='center', va='center', rotation='vertical', fontsize=18)
fig.subplots_adjust(bottom=0.11, right=0.95, wspace=0.35)
plt.locator_params(axis = 'y', nbins = len(accumprox))
sns.despine()
plt.savefig("%s_proxies_barplot.png" % prefix, dpi=300)
plt.close()


#arrange the various dataframes and save to files
(stratigraphy - stratigraphy.ix[:,stratum][RunLength]).T.to_csv("%s_stratigraphy.csv" % prefix) # NOW change the stratigraphy to depth below surface, transpose, and save it out
accumprox.to_csv("%s_proxies.csv" % prefix) # save out the proxies dataframe
print "Done!"


