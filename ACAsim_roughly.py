import shutil
import numpy as np
intt=['10s','20s','30s']
PB=['0.3PB','0.5PB','0.7PB']
tott=['1','2','3']
antlist=['1','2','3']
for intt in intt :
 for PB in PB :
  for antlist in antlist :
   for tott in tott :
    # Set simobserve to default parameters
    default("simobserve")
    # Our project name will be no1, and all simulation products will be placed in a subdirectory no1/
    project="no1_%s_%s_%s_%s"  %(intt,PB,tott,antlist)
    skymodel = "no1flux.fits"
    # Set model image parameters:
    indirection="J2000 10h00m00.0s -30d00m00.0s"
    incell="1arcsec"
    inbright="0.00017582203080812763"
    incenter="100GHz"
    inwidth="10MHz"
    # Sim 12m interferometric
    #have simob calculater mosaic pointing locations 
    setpointings       =  True
    integration        =  intt
    mapsize            =  "4arcmin"
    maptype            =  "ALMA"
    pointingspacing    =  PB      # "0.5PB" or '***arcsec'
    #calculater vis
    obsmode            =  "int"
    antennalist        =  "alma.cycle5.%s.cfg" %antlist
    totaltime          =  tott
    graphics           =  "both"
    simobserve()
 
    # Sim 12m total power(TP) obs
    integration        =  intt
    mapsize            =  "6arcmin" # has to be larger than inter
    maptype            =  "square"
    obsmode            = "sd"
    sdantlist          = "aca.tp.cfg"
    sdant              = 0
    refdate            = "2018/12/01"
    totaltime          =  tott
    simobserve()
 
    #Sim 7m ACA obs
    integration        =  intt
    mapsize            =  "4arcmin"
    maptype            =  "ALMA"
    pointingspacing    =  PB
    obsmode            = "int"
    refdate            = "2018/12/02"
    antennalist        =  "aca.i.cfg"
    totaltime          =  tott
    simobserve()


    #First image total power and ACA with total power as a model
    default("simanalyze")
    project            =  "no1_%s_%s_%s_%s"  %(intt,PB,tott,antlist)
    vis                =  '$project.aca.i.ms,$project.aca.tp.sd.ms' 
    imsize             =  [512,512]
    cell               =  ''
    analyze            =  True
    showpsf            =  False
    showresidual       =  False
    showconvolved      =  True
    simanalyze()
 
    #Next add the 12m interferometric data
    default("simanalyze")
    project            =  "no1_%s_%s_%s_%s"  %(intt,PB,tott,antlist)
    vis                =  '$project.alma.cycle5.%s.ms' %antlist
    imsize             =  [512,512]
    cell               =  ''
    modelimage         =  "$project.aca.i.image" 
    analyze            =  True
    showpsf            =  False
    showresidual       =  False
    showconvolved      =  True
    simanalyze()
    shutil.copy('no1_%s_%s_%s_%s/no1_%s_%s_%s_%s.alma.cycle5.%s.analysis.png' %(intt,PB,tott,antlist,intt,PB,tott,antlist,antlist),'analysispng/no1_%s_%s_%s_%s.png' %(intt,PB,tott,antlist))
