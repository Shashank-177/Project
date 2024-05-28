# Data analysis process (see in raw)

IXPEOBSSIM:

The package is written in python script for the purpose of data analysis of the IXPE data. The workflow of the analysis is as follows:

1. The fits file of the source for 3 detectors are obtained from - https://heasarc.gsfc.nasa.gov/cgi-bin/W3Browse/w3browse.pl.

2. Import the ixpeobbsim package and the fits files in the script.
  from ixpeobssim import IXPEOBSSIM_CONFIG
  import ixpeobssim .core. pipeline as pipeline
  from ixpeobssim .binning. polarization import xBinnedPolarizationCube

3. Using the xpselect option in the ixpeobssim package, give the source and background region and specify the fits file path. This is to be done for each detector.
   src_file_list = pipeline.xpselect (file_path , rad=SRC_RAD , suffix='src', overwrite = OVERWRITE )
   bkg_file_list = pipeline.xpselect (file_path ,innerrad=BKG_INNER_RAD , rad=BKG_OUTER_RAD ,suffix='bkg', overwrite = OVERWRITE )

4. In xpbin, choose the required algorithm such as PHA1, PHA1Q, PHA1U to generate spectras of stokes parameters I, Q and U respectively or PCUBE to generate polarization cube. The source and background fits file generated by xpselect are given in the command. For the irf files, ixpeobssim package has it's own set of response files that being updated with the updates in CALDB. So the path of the irf files can be given where these response files are stored in the package. Also update the package as soon as the updates are announced they update the response files also as CALDB is updated.
  # Example for algorithm 'PCUBE', similarly can be done for 'PHA' algorithm
  kwargs = dict( algorithm ='PCUBE', ebinalg='LIST',ebinning=ENERGY_BINNING , overwrite = OVERWRITE,irfname = 'ixpe:obssim:v12')
  src_pcube_file_list = pipeline.xpbin (*src_file_list, ** kwargs,mc= False)
  bkg_pcube_file_list = pipeline.xpbin (*bkg_file_list, ** kwargs,mc = False)
  # creating polarization cube:
  src_pcube = xBinnedPolarizationCube . from_file_list (src_pcube_file_list )
  bkg_pcube = xBinnedPolarizationCube . from_file_list (bkg_pcube_file_list )
  bkg_pcube *= src_pcube .backscal () / bkg_pcube .backscal ()
  src_pcube -= bkg_pcube
  
5. Then the pcube can be printed and various representation of polarization parameters can be done. For the spectra, the background subtraction can be done in HEASoft.
6. After subtracting the background the modelling can be done in Xspec in HEASoft. Once you know the model and obtained a low reduced chi squared fit note the parameters.

