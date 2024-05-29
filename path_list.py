import os

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from ixpeobssim import IXPEOBSSIM_CONFIG
import ixpeobssim .core. pipeline as pipeline
from ixpeobssim .binning. polarization import xBinnedPolarizationCube

#CFG_FILE_PATH = os.path.join( IXPEOBSSIM_CONFIG , 'toy_softwarex.py')
#DURATION = 20000.
 # Global flag ---toggle this not to overwriteexisting files.
OVERWRITE = True
# Region selection: the source is a circular patch ,while the background is a larger annuluscentered
# in the same position (by default the referenceposition in the WCS of the original event file)

# All radii are in arcmin.pip
SRC_RAD = 1
BKG_INNER_RAD = 3
BKG_OUTER_RAD = 4
# Energy binning for the polarization cubes.
ENERGY_BINNING = np.array ([2. ,3.5 ,5., 6.5, 8.])

#Read the path to the source files for different detectors, note the file name of the event name is edited
file_path = "/Users/shash/Desktop/XRB/4U1630-472_2022/01250401/event_l2/ixpe01250401_det1_evt2_v03/DU1.fits"
file_path2 = "/Users/shash/Desktop/XRB/4U1630-472_2022/01250401/event_l2/ixpe01250401_det2_evt2_v03/DU2.fits"
file_path3 = "/Users/shash/Desktop/XRB/4U1630-472_2022/01250401/event_l2/ixpe01250401_det3_evt2_v03/DU3.fits"

#Source and background list file for detector 1 
src_file_list = pipeline.xpselect (file_path , rad=SRC_RAD , suffix='src', overwrite = OVERWRITE )
bkg_file_list = pipeline.xpselect (file_path ,innerrad=BKG_INNER_RAD , rad=BKG_OUTER_RAD ,suffix='bkg', overwrite = OVERWRITE )

src_file_list2 = pipeline.xpselect (file_path2 , rad=SRC_RAD , suffix='src', overwrite = OVERWRITE )
bkg_file_list2= pipeline.xpselect (file_path2 ,innerrad=BKG_INNER_RAD , rad=BKG_OUTER_RAD ,suffix='bkg', overwrite = OVERWRITE )

src_file_list3 = pipeline.xpselect (file_path3 , rad=SRC_RAD , suffix='src', overwrite = OVERWRITE )
bkg_file_list3 = pipeline.xpselect (file_path3 ,innerrad=BKG_INNER_RAD , rad=BKG_OUTER_RAD ,suffix='bkg', overwrite = OVERWRITE )



