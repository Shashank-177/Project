import numpy as np #and all the imports from path_list.py

kwargs = dict( algorithm ='PCUBE', ebinalg='LIST',ebinning=ENERGY_BINNING , overwrite = OVERWRITE,irfname = 'ixpe:obssim:v12')
src_pcube_file_list = pipeline.xpbin (*src_file_list, ** kwargs,mc= False)
bkg_pcube_file_list = pipeline.xpbin (*bkg_file_list, ** kwargs,mc = False)

kwargs = dict( algorithm ='PCUBE', ebinalg='LIST',ebinning=ENERGY_BINNING , overwrite = OVERWRITE,irfname = 'ixpe:obssim:v12')
src_pcube_file_list2 = pipeline.xpbin (*src_file_list2, ** kwargs,mc= False)
bkg_pcube_file_list2 = pipeline.xpbin (*bkg_file_list2, ** kwargs,mc = False)

kwargs = dict( algorithm ='PCUBE', ebinalg='LIST',ebinning=ENERGY_BINNING , overwrite = OVERWRITE,irfname = 'ixpe:obssim:v12')
src_pcube_file_list3 = pipeline.xpbin (*src_file_list3, ** kwargs,mc= False)
bkg_pcube_file_list3 = pipeline.xpbin (*bkg_file_list3, ** kwargs,mc = False)

# Read back the polarization cubes and perform the background subtraction.
src_pcube = xBinnedPolarizationCube . from_file_list (src_pcube_file_list )
bkg_pcube = xBinnedPolarizationCube . from_file_list (bkg_pcube_file_list )
bkg_pcube *= src_pcube .backscal () / bkg_pcube .backscal ()
src_pcube -= bkg_pcube

src_pcube2 = xBinnedPolarizationCube . from_file_list (src_pcube_file_list2 )
bkg_pcube2 = xBinnedPolarizationCube . from_file_list (bkg_pcube_file_list2 )
bkg_pcube2 *= src_pcube2.backscal () / bkg_pcube2 .backscal ()
src_pcube2 -= bkg_pcube2

src_pcube3 = xBinnedPolarizationCube . from_file_list (src_pcube_file_list3 )
bkg_pcube3 = xBinnedPolarizationCube . from_file_list (bkg_pcube_file_list3 )
bkg_pcube3 *= src_pcube3.backscal () / bkg_pcube3 .backscal ()
src_pcube3 -= bkg_pcube3

print('Polarization degree : ', src_pcube .PD)
print('Polarization degree error :' ,src_pcube .PD_ERR)
print('Polarization angle : ', src_pcube .PA , 'deg')
print('Polarization angle error : ', src_pcube .PA_ERR , 'deg')

print('Polarization degree2 : ', src_pcube2 .PD)
print('Polarization degree error2 :' , src_pcube2 .PD_ERR)
print('Polarization angle2 : ', src_pcube2 .PA , 'deg')
print('Polarization angle error2 : ', src_pcube2 .PA_ERR , 'deg')

print('Polarization degree3 : ', src_pcube3 .PD)
print('Polarization degree error3 :' , src_pcube3 .PD_ERR)
print('Polarization angle3 : ', src_pcube3 .PA , 'deg')
print('Polarization angle error3 : ', src_pcube3 .PA_ERR , 'deg')
