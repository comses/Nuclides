#Quick Cosmogenic Nuclide Production as basis for proxies in Medland

#Production of a cosmogenic nuclide follows the same laws for hillslope bedrock and sediment and channels, but the history (inheritance) may be different. Essentially two processes: Production, and sediment transport.

#Goal: Calculate production rate for sediment, soil, and bedrock.

#Simplifications: Only accounts for spallation with oxygen in quartz as a way of producing Be-10. We could add more nuance but it's not important for faster erosion rates...
#We are ignoring inheritance. This means the model has to run for some time before perturbing it, or at least adding the caveat that this is the CHANGE in nuclide concentration.

#Nuclide-dependent parameters:
P_0 	 = 4.49		# [at/g/yr] after Stone, 1999. Prodcution rate of Beryllium-10 in quartz on the surface at sea level,
ltlambda = log(2)/1.5e6	#little lambda, decay constant for Be-10
L 		 = 160 			#absorption mean-free path (attenuation length) [g/cm2].



#Sample-dependent parameters:
p 	 		= 2.6 			#density of overburden, [ g/cm3]
topo_shld	= 1		#topographic shielding factor, varies between 0 (completely shielded) to 1 (not shielded)
latitude	= 40			#latitude, Mediterranean
longitude  	= 0 			#Longitude, Mediterranean

#Parameters that change with time and come from the model
#N is the concentration of nuclides in the sample.
#z is the depth to that packet of sediment at time t
#t is some length of time.

N <-.5
z <- 1:100
P_z <- P_0 * exp(-z*L/p) - N*ltlambda

plot(P_z)
#Note: z, N are functions of time. P_z is the production rate, and can be applied for some delta t as the change in nuclide concentration for that time.
