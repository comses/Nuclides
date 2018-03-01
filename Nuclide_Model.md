---
title: "Spatially-explicit model of cosmogenic nuclide production in sediments"
author: "Nicolas Gauthier and Nari Miller"
date: "Last updated: February, 2018"
output:
  html_document: 
    keep_md: yes
  pdf_document:
    highlight: zenburn
---




```r
library(tidyverse)
library(stringr)
library(rgrass7)
```

## Model specification
We use the following model for $P_z$, the production rate of $^{10}$Be at depth $z$:  
$$P_z = P_0 e^{-z\frac{\rho}{\Lambda_{spal}}} - N\lambda$$  
with parameters:  

$P_0$ is the production rate of Beryllium-10 in quartz at sea level

```r
P_0 <- 4.49		# [at/g/yr] after Stone, 1999.
```

$\lambda$ is the decay constant for $^{10}$Be

```r
ltlambda <- log(2) / 1.5e6
```

$L$ is the attenuation length for neutrons

```r
L <- 160 	# [g/cm2]
```

$\rho$ is the density of overburden

```r
rho <- 2.6 	# [ g/cm3]
```

and variables:

$N$ is the concentration of nuclides in the sample  
$z$ is the depth to that packet of sediment at time $t$   
$t$ is some length of time.  

### Assumptions  
For the sake of simplicity, we assume there is no topographic shielding (topographic shielding factor = 1) and a constant location in the Mediterranean at 40N 0E.


## Sample data
First we need base set of raster maps to initialize the variables.  
We create a multi-layer raster brick where each cell represents a 1 cm$^{3}$ packet of sediment, the **values()** of the cells correspond to $N$ (the concentration of nuclides in that packet), and the index of each layer corresponds to $1 + z$, the depth of that packet of sediment in cm.  

Lets create a sample raster brick with 5 layers of 1x1 cells, with an initial value of $N = 1$ for each cell.  

```r
N0 <- rep(1, 1000)
```

## Simulation
First translate the above formula for $P_z$ into an R function that calculates the $^{10}$Be production rate given values of $N$ and $z$.

```r
P_z <- function(N, z){
  P_0 * exp(-z*rho/L) * exp(-ltlambda) - N*ltlambda
}
```

Numerically integrate the differential equation with Euler's method. Using this function and the sample raster brick, iterate over a period of 100 years.

```r
nsim <- 100 # simulation length

N <- N0 # initial conditions

record <- data_frame(time = 0, depth = 1:length(N) - .5, value = N)

for(i in 1:nsim){
  delta <- P_z(N, (1:length(N) - .5))
  N <- N + delta
  record <- data_frame(time = i, depth = 1:length(N) - .5, value = N) %>%
    bind_rows(record, .)
}
```

Plot the resulting solution.

```r
ggplot(record, aes(x=time, y=value, group = as.factor(depth), color = depth)) + 
  geom_line() +
  scale_color_distiller(palette = 'Spectral', name = 'Depth (cm)') +
  labs(title = 'Nuclide concentration over time, at multiple depths', subtitle = 'No erosion', x = 'Time (years)', y = 'Concentration (at/g)') +
  theme_minimal()
```

![](Nuclide_Model_files/figure-html/unnamed-chunk-9-1.png)<!-- -->


```r
record %>%
  filter(depth <= 500) %>%
ggplot(aes(x=value, y=depth * -1, group = as.factor(time), color = time)) + 
  geom_line() + 
  scale_color_distiller(palette = 'Spectral', name = 'Time (years)') +
  labs(title = 'Nuclide concentration depth profiles with time', subtitle = 'No erosion', x = 'Concentration (at/g)', y = 'Depth (cm)') +
  theme_minimal()
```

![](Nuclide_Model_files/figure-html/unnamed-chunk-10-1.png)<!-- -->

Now rerun the simulation, adding a constant erosion rate.

```r
N <- N0 # initial conditions
nsim <- 300
record <- data_frame(time = 0, depth = 1:length(N) - .5, value = N)
for(i in 1:nsim){
  delta <- P_z(N, (1:length(N) - .5))
  N <- N + delta
  N <- N[-1] ; N <- c(N,1)
  record <- data_frame(time = i, depth = 1:length(N) - .5, value = N) %>%
    bind_rows(record, .)
}
```

We can see that, with constant erosion, nuclide concentrations reach and equilibrium point.

```r
ggplot(record, aes(x=time, y=value, group = as.factor(depth), color = depth)) + 
  geom_line() +
  scale_color_distiller(palette = 'Spectral', name = 'Depth (cm)') +
  labs(title = 'Nuclide concentration over time, at multiple depths', subtitle = 'Erosion = 1 cm/yr', x = 'Time (years)', y = 'Concentration (at/g)') +
  theme_minimal()
```

![](Nuclide_Model_files/figure-html/unnamed-chunk-12-1.png)<!-- -->

Likewise, we can see that an equilibrium depth profile is reached.

```r
ggplot(record, aes(x=value, y=depth * -1, group = as.factor(time), color = time)) + 
  geom_line() + 
  scale_color_distiller(palette = 'Spectral', name = 'Time (years)') +
  labs(title = 'Nuclide concentration depth profiles with time', subtitle = 'Erosion = 1cm/yr', x = 'Concentration (at/g)', y = 'Depth (cm)') +
  theme_minimal()
```

![](Nuclide_Model_files/figure-html/unnamed-chunk-13-1.png)<!-- -->

What if erosion varies over time?

```r
set.seed(1000) # set seed for reproduceability
erosion <- runif(nsim, max = 2) %>% #randomly generate a series of erosion and deposition rates
  as.integer

N <- N0 # initial conditions
record <- data_frame(time = 0, depth = 1:length(N) - .5, value = N)
for(i in 1:nsim){
  delta <- P_z(N, (1:length(N) - .5))
  N <- N + delta
  e <- erosion[i]
  if(e > 0){N = N[-(1:e)]}
  record <- data_frame(time = i, depth = 1:length(N) - .5, value = N) %>%
    bind_rows(record, .)
}
```


```r
ggplot(record, aes(x=time, y=value, group = as.factor(depth), color = depth)) + 
  geom_line() +
  scale_color_distiller(palette = 'Spectral', name = 'Depth (cm)') +
  labs(title = 'Nuclide concentration over time, at multiple depths', subtitle = 'Variable erosion', x = 'Time (years)', y = 'Concentration (at/g)') +
  theme_minimal()
```

![](Nuclide_Model_files/figure-html/unnamed-chunk-15-1.png)<!-- -->


```r
ggplot(record, aes(x=value, y=depth * -1, group = as.factor(time), color = time)) + 
  geom_line(alpha = .1) + 
  scale_color_distiller(palette = 'Spectral', name = 'Time (years)') +
  labs(title = 'Nuclide concentration depth profiles with time', subtitle = 'Variable erosion', x = 'Concentration (at/g)', y = 'Depth (cm)') +
  theme_minimal()
```

![](Nuclide_Model_files/figure-html/unnamed-chunk-16-1.png)<!-- -->

Now include variable erosion AND deposition

```r
erosion <- rnorm(nsim, mean = -1, sd = 1.5) %>% #randomly generate a series of erosion and deposition rates
  as.integer

N <- N0 # initial conditions
record <- data_frame(time = 0, depth = 1:length(N) - .5, value = N)
for(i in 1:nsim){
  delta <- P_z(N, (1:length(N) - .5))
  N <- N + delta
  e <- erosion[i]
  if(e > 0){N <- c(rep(1, e), N)} 
  if(e < 0){N = N[-(1:abs(e))]} 
  record <- data_frame(time = i, depth = 1:length(N) - .5, value = N) %>%
    bind_rows(record, .)
}
```


```r
ggplot(record, aes(x=time, y=value, group = as.factor(depth), color = depth)) + 
  geom_line(alpha = .5) +
  scale_color_distiller(palette = 'Spectral', name = 'Depth (cm)') +
  labs(title = 'Nuclide concentration over time, at multiple depths', subtitle = 'Variable erosion and depostion', x = 'Time (years)', y = 'Concentration (at/g)') +
  theme_minimal()
```

![](Nuclide_Model_files/figure-html/unnamed-chunk-18-1.png)<!-- -->


```r
ggplot(record, aes(x=value, y=depth * -1, group = as.factor(time), color = time)) + 
  geom_line(alpha = .1) + 
  scale_color_distiller(palette = 'Spectral', name = 'Time (years)') +
  labs(title = 'Nuclide concentration depth profiles with time', subtitle = 'Variable erosion and deposition', x = 'Concentration (at/g)', y = 'Depth (cm)') +
  theme_minimal()
```

![](Nuclide_Model_files/figure-html/unnamed-chunk-19-1.png)<!-- -->

## Working in GRASS
Use the rgrass7 library to try doing the same thing in GRASS, using a realistic DEM. *Note* for the following to work, R must be called from an active GRASS session.

First define the coordinates of our virtual sediment core. Its important to select a meaningful point given the spatial distribution of erosion and deposition. Also define an initial value for the nuclide concentrations, and a length for the simulation to last.

```r
core.pt <- c(725763.609242,4284801.3547)  # location of the virtual sediment core
init <- 1 # inital nuclide value
nsim <- 50
```

Now define some map names representing raster that already exist in GRASS, namely the DEM and bedrock maps used in r.landscape_evol. Use these to setup and execute a command in r.mapcalc that calculates the depth to bedrock of every cell in the DEM.

```r
elev_init <- 'DEM'
bedrock <- 'bedrock'

expr <- paste0(c('soildepth_init = if(', elev_init, ' - ', bedrock, ' < 0, 0, ', elev_init, ' - ', bedrock, ')'), collapse = '')
execGRASS('r.mapcalc', flags = c('overwrite'), expression = expr)
```

Use this soil depth map to create a dataframe in R, where each row corresponds to a cell of the raster. Within each row of this dataframe, the column named *soil_column* contains a vector whose length corresponds to the soil depth, in centimeters, with each value set to the initial nuclide value defined above.

```r
init_depths <- readRAST('soildepth_init') %>% # pull in raster from grass as spatial grid data frame
  as_tibble %>% # convert to tibble
  filter(soildepth_init > 0) %>%  # remove null cells
  rename(x = s1, y = s2) %>%  # rename the location columns
  mutate(depth_cm = as.integer(soildepth_init * 100)) %>% # convert depths from m to cm, then to integers
  mutate(soil_column = map(depth_cm, ~ rep.int(init, .x))) %>% # make soil columns of length depth with value init value
  select(-soildepth_init)
```

```
## Creating BIL support files...
## Exporting raster as floating values (bytes=8)
##    0%   3%   6%   9%  12%  15%  18%  21%  24%  27%  30%  33%  36%  39%  42%  45%  48%  51%  54%  57%  60%  63%  66%  69%  72%  75%  78%  81%  84%  87%  90%  93%  96%  99% 100%
```

```r
init_depths
```

```
## # A tibble: 211,293 x 4
##         x       y depth_cm soil_column  
##     <dbl>   <dbl>    <int> <list>       
##  1 725825 4286059     1836 <dbl [1,836]>
##  2 725835 4286059     1807 <dbl [1,807]>
##  3 725845 4286059     1780 <dbl [1,780]>
##  4 725855 4286059     1757 <dbl [1,757]>
##  5 725865 4286059     1737 <dbl [1,737]>
##  6 725875 4286059     1722 <dbl [1,722]>
##  7 725885 4286059     1711 <dbl [1,711]>
##  8 725895 4286059     1704 <dbl [1,704]>
##  9 725905 4286059     1702 <dbl [1,702]>
## 10 725915 4286059     1704 <dbl [1,704]>
## # ... with 211,283 more rows
```

Now we've set up our basic model domain, an irregular three dimensional grid of cubic centimeter sized cells, represented as a nested data frame. We can apply the nuclide function to each column in turn, just as in the one dimensional case above.

```r
init_depths %>% 
  mutate(soil_column = map2(soil_column, depth_cm, ~ .x + P_z(.x, 1:.y - .5)))
```

```
## # A tibble: 211,293 x 4
##         x       y depth_cm soil_column  
##     <dbl>   <dbl>    <int> <list>       
##  1 725825 4286059     1836 <dbl [1,836]>
##  2 725835 4286059     1807 <dbl [1,807]>
##  3 725845 4286059     1780 <dbl [1,780]>
##  4 725855 4286059     1757 <dbl [1,757]>
##  5 725865 4286059     1737 <dbl [1,737]>
##  6 725875 4286059     1722 <dbl [1,722]>
##  7 725885 4286059     1711 <dbl [1,711]>
##  8 725895 4286059     1704 <dbl [1,704]>
##  9 725905 4286059     1702 <dbl [1,702]>
## 10 725915 4286059     1704 <dbl [1,704]>
## # ... with 211,283 more rows
```
As before, let's add in time varying erosion and deposition. This time, we'll use ED information from a previous run of r.landscape_evol. We'll campre ED maps from three different land cover experiments to see how our method performs in different erosional contexts.

First list out the ED rate maps for three different land cover experiments.

```r
edmaps <- execGRASS('g.list', flags = c('m'), type='rast', pattern='levol_ED_rate*', separator=',', intern = T) %>%
  str_split(',', simplify = T)
edmaps.bare <- execGRASS('g.list', flags = c('m'), type='rast', pattern='levol_bare_ED_rate*', separator=',', intern = T) %>%
  str_split(',', simplify = T)
edmaps.forest <- execGRASS('g.list', flags = c('m'), type='rast', pattern='levol_forest_ED_rate*', separator=',', intern = T) %>%
  str_split(',', simplify = T)
```

Then add them all together and plot the results

```r
execGRASS('r.series', flags = c('overwrite'), input = edmaps, output = 'erosion_total', method = 'sum')
```

```
##    0%   3%   6%   9%  12%  15%  18%  21%  24%  27%  30%  33%  36%  39%  42%  45%  48%  51%  54%  57%  60%  63%  66%  69%  72%  75%  78%  81%  84%  87%  90%  93%  96%  99% 100%
```

```r
execGRASS('r.series', flags = c('overwrite'), input = edmaps.bare, output = 'erosion_total_bare', method = 'sum')
```

```
##    0%   3%   6%   9%  12%  15%  18%  21%  24%  27%  30%  33%  36%  39%  42%  45%  48%  51%  54%  57%  60%  63%  66%  69%  72%  75%  78%  81%  84%  87%  90%  93%  96%  99% 100%
```

```r
execGRASS('r.series', flags = c('overwrite'), input = edmaps.forest, output = 'erosion_total_forest', method = 'sum')
```

```
##    0%   3%   6%   9%  12%  15%  18%  21%  24%  27%  30%  33%  36%  39%  42%  45%  48%  51%  54%  57%  60%  63%  66%  69%  72%  75%  78%  81%  84%  87%  90%  93%  96%  99% 100%
```

```r
erosion_dat <- bind_cols(readRAST('erosion_total') %>% as_tibble,
                         readRAST('erosion_total_bare') %>% as_tibble,
                         readRAST('erosion_total_forest') %>% as_tibble) %>%
  select(x = s1, y = s2, grass = erosion_total, bare = erosion_total_bare, forest = erosion_total_forest) %>%
  gather(key = 'landcover', value = 'erosion', -x, -y) %>%
  mutate(erosion = erosion * 100)  # convert meters to centimeters
```

```
## Creating BIL support files...
## Exporting raster as floating values (bytes=8)
##    0%   3%   6%   9%  12%  15%  18%  21%  24%  27%  30%  33%  36%  39%  42%  45%  48%  51%  54%  57%  60%  63%  66%  69%  72%  75%  78%  81%  84%  87%  90%  93%  96%  99% 100%
## Creating BIL support files...
## Exporting raster as floating values (bytes=8)
##    0%   3%   6%   9%  12%  15%  18%  21%  24%  27%  30%  33%  36%  39%  42%  45%  48%  51%  54%  57%  60%  63%  66%  69%  72%  75%  78%  81%  84%  87%  90%  93%  96%  99% 100%
## Creating BIL support files...
## Exporting raster as floating values (bytes=8)
##    0%   3%   6%   9%  12%  15%  18%  21%  24%  27%  30%  33%  36%  39%  42%  45%  48%  51%  54%  57%  60%  63%  66%  69%  72%  75%  78%  81%  84%  87%  90%  93%  96%  99% 100%
```

```r
ggplot(erosion_dat, aes(x, y)) +
  facet_wrap(~ landcover) +
  geom_raster(aes(fill = erosion)) +
  scale_fill_distiller(type = 'div', limits = c(-15,15), name = 'Elevation change (cm)') +
  geom_point(x = core.pt[1], y = core.pt[2]) +
  labs(title = 'Net erosion and deposition after 50 years', subtitle = 'Under varying land covers') +
  theme_void() +
  coord_equal()
```

![](Nuclide_Model_files/figure-html/unnamed-chunk-25-1.png)<!-- -->


```r
# loop thru simulation outputs, generating the local watershed from each elevation map, add together into a master watershed 
elevmaps <- execGRASS('g.list', flags = c('m'), type='rast', pattern='levol_elevation*', separator=',', intern = T) %>%
  str_split(',', simplify = T)
for(i in 1:nsim){
  execGRASS('r.watershed', flags = c('quiet', 'overwrite'), elevation = elevmaps[i], drainage = 'fldr_tmp')
  execGRASS('r.water.outlet', flags = c('quiet', 'overwrite'), input = 'fldr_tmp', output = paste0('basin_tmp_', i), coordinates = core.pt)
  execGRASS('r.mapcalc', flags = c('overwrite'), expression = 'basin_tmp = if(isnull(basin_tmp), 0, 1)')
}

basinmaps <- execGRASS('g.list', flags = c('m'), type = 'rast', pattern = 'basin_tmp_*', separator = ',', intern = T) %>%
  str_split(',', simplify = T)

execGRASS('r.series', flags = c('overwrite'), input = basinmaps, output = 'basin_all', method = 'sum')
```

```
##    0%   3%   6%   9%  12%  15%  18%  21%  24%  27%  30%  33%  36%  39%  42%  45%  48%  51%  54%  57%  60%  63%  66%  69%  72%  75%  78%  81%  84%  87%  90%  93%  96%  99% 100%
```

```r
#execGRASS('r.mask', raster = 'basin_tmp', flags = c('overwrite'))
readRAST('basin_all') %>% plot
```

```
## Creating BIL support files...
## Exporting raster as floating values (bytes=8)
##    0%   3%   6%   9%  12%  15%  18%  21%  24%  27%  30%  33%  36%  39%  42%  45%  48%  51%  54%  57%  60%  63%  66%  69%  72%  75%  78%  81%  84%  87%  90%  93%  96%  99% 100%
```

![](Nuclide_Model_files/figure-html/unnamed-chunk-26-1.png)<!-- -->

```r
# so most cells are in the watershed all 50 years

mask <- readRAST('basin_all') %>% 
  as_tibble %>%
  select(x = s1, y = s2)
```

```
## Creating BIL support files...
## Exporting raster as floating values (bytes=8)
##    0%   3%   6%   9%  12%  15%  18%  21%  24%  27%  30%  33%  36%  39%  42%  45%  48%  51%  54%  57%  60%  63%  66%  69%  72%  75%  78%  81%  84%  87%  90%  93%  96%  99% 100%
```

```r
semi_join(init_depths, mask) # extract only the soil columns that are in any of the simulation watershed
```

```
## # A tibble: 144,627 x 4
##         x       y depth_cm soil_column  
##     <dbl>   <dbl>    <int> <list>       
##  1 723545 4285659     1197 <dbl [1,197]>
##  2 723625 4285659      866 <dbl [866]>  
##  3 723635 4285659      821 <dbl [821]>  
##  4 723685 4285659      706 <dbl [706]>  
##  5 723695 4285659      693 <dbl [693]>  
##  6 723705 4285659      682 <dbl [682]>  
##  7 723545 4285649     1189 <dbl [1,189]>
##  8 723555 4285649     1158 <dbl [1,158]>
##  9 723565 4285649     1117 <dbl [1,117]>
## 10 723575 4285649     1072 <dbl [1,072]>
## # ... with 144,617 more rows
```



```r
#sample the erosion and deposition maps at core coordinates, convert to centimeters
# we'll start with the bare ground case, because deposition is high enough we don't have to worry about numerical instability yet
execGRASS('r.what', map = edmaps.bare, coordinates = core.pt, separator = ',', intern = T) %>%
  str_split(',', simplify = T) %>%
  .[,-(1:3)] %>%
  as.numeric %>%
  `*`(100) %>% # meters to cm
  tibble(year = 1:100, elev_change = .)
```

```
## # A tibble: 100 x 2
##     year elev_change
##    <int>       <dbl>
##  1     1        7.24
##  2     2        4.62
##  3     3        4.73
##  4     4        4.99
##  5     5        5.28
##  6     6        5.74
##  7     7        6.26
##  8     8        6.00
##  9     9        5.68
## 10    10        5.66
## # ... with 90 more rows
```

```r
#execGRASS('r.mask', flags = c('r'))
```


Select a point

for each time step:
  if erosion rate is positive:
    subtract that depth from nuclide profile
  if deposition rate is positive:
    get drainage direction map
    calculate watershed at that point using r.water.outlet
    get all the cells in that watershed
    add up the nucldie enrichment of all the cells that eroded in the watershed, average based on the depth of erosion
    add that value of nuclide in the depth of deposition  at that area.
