# Set simobserve to default parameters
default("simobserve")
# Our project name will be no1, and all simulation products will be placed in a subdirectory no1/
project="no1"
skymodel =  "no1flux.fits"
# Set model image parameters:
indirection="B1950 23h59m59.96s -34d59m59.50s"
incell="0.1arcsec"
inbright="0.004"
incenter="330.076GHz"
inwidth="50MHz"
# have simobserve calculate mosaic pointing locations:
setpointings       =  True
integration        =  "10s"
mapsize            =  "1arcmin"
maptype            =  "hex"
pointingspacing    =  "9arcsec"      # this could also be specified in units of the primary beam e.g. "0.5PB"
obsmode            =  "int"
antennalist        =  "ALMA;0.5arcsec"
totaltime          =  "3600s"
graphics           =  "both"
simobserve()
