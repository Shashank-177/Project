Simulation (see in raw)

The corona geometry of the black hole sources are simulated using the Monte Carlo radiative transfer code(Monk). The process that has to be followed is as:

1. The monk code can be downloaded from https://projects.asu.cas.cz/zhang/monk.
2. The system should have the follwoing requirements: 
- GNU Make
- C++ compiler that supports c++14 standard; for GCC starting from GCC 5.3
- MPI library
- libstdc++fs; included in GCC starting from GCC 5.3
3. In the virgo cluster the module openmpi is installed, to use the mpirun required in the installation, the module is to be loaded as
  module load gnu12/12.2.0  #dependency
  module load openmpi4/4.1.4
4. The installation process is as follows:
  1. build `sim5` library under ./sim5
     ```
    cd sim5
    make
     
  2. modify line 17 of `electron_population.h` to set the correct value of
   `hotdir`, the path to the directory that contains ``logthetat.dat`, `logx.dat`, and `hotx.dat`, the
   data files that are used to save hot Klein-Nishina cross section. I put them
   in `./data`, but you have to use the absoluate path.
	
  3. edit `Makefile` to assign the appropriate values to the following variables:
	- `SIM5INC`: path to directory that contains `sim5lib.h`
	- `SIM5OBJ`: path to `sim5lib.o`
	- `OBJDIR`: directory for object file
	- `BINDIR`: directory for binary files
	- `TRASHDIR`: directory for trash
	- `INSTALLDIR`: directory where you put executable binaries
  5. `make objs` to build objects
  6. `make 3dcorona 3dcorona_mpi calspec`

5. For the usage the readme file of the monk can be followed.
6. General tips for the commands:
   cd /working/directory/
   /home/path_to_monk/bin/3dcorona para1.txt      # where para1.txt is the parameter file containing geometrical information given as an input for the 3dcorona geodesic calculation code
   cd disc
   /home/path_to_monk/bin/3dcorona para2.txt      # where para2.txt is the parameter file with type = 1 (sampling the photons)
   cd corona
   mpirun -n 4 /home/path_to_monk/bin/3dcorona_mpi para3.txt  #when running in the system or workstation, increase the number of cores for faster computation. Para3 is the input parameter 
                                                              #file containing the physical parameters such as mass,accretion rate, optical depth and coronal temperature.
7. For running in cluster, create a shell file as:
   #!/bin/bash
  #SBATCH -N 2                                                            # N denotes no. of nodes
  #SBATCH --ntasks-per-node=16                                            # denotes no. of cores per node
  #SBATCH -J 3dcorona                                                     # denotes job name
  #SBATCH -p iist                                                         # denotes partition 
  #SBATCH --time=24:00:00                                                 # denotes uptime for run
  #SBATCH -o slurm.%N.%j.out # STDOUT                                     # denotes the output file
  #SBATCH -e slurm.%N.%j.err # STDERR                                     # denotes the error file
  #SBATCH --export=all
  
  cd $SLURM_SUBMIT_DIR
  
  mpirun -n 32 /home/shashank/Shashank/monk-master/bin/3dcorona_mpi para3.txt    

8. For submitting the job in the cluster use:
   sbatch submit.sh                                                       # submit.sh is the name of the created shell file.

9. For running calspec command:
   cd working_directory
   /home/path_to_monk-master/bin/calspec /home/path_to_inf_directory/ n en_min en_max inc_min inc_max    # where path to inf is the path where the inf directory is created where the files
                                                                                                          # from the 3dcorona_mpi is located, n is the no. of bins, en_min and en_max is the 
                                                                                                           # minimum and maximum of the energy values in kev, inc_min and inc_max is the 
                                                                                                            # minimmum and maximum value of the inclination angle in deg.
                                                                                  
Examples of all the parameter files:

Spherical case:
parameter 1 file:
[physical]
# black hole spin
a = 0.933
# the geometry of the corona; 0 for stationary spherical coronae;
gtype = 0
# the height of the corona
h = 10.
# radius of the corona
radius = 9
# inner edge of the disc, in GM/c^2; if rin < rms, then rin = rms
rin = 1.3
# outer edge of the disc, in GM/c^2
rout = 1000.

[gridsize]
# number of radial bins on the disc
nr = 100
# number of bins in the polar emission angle of the seed photon
nphi = 100
# number of bins in the azimuthal emission angle of the seed photon
ntheta = 100
# the maximum polar emission angle over PI; 0.5 means the maximum angle is half
# PI
thetamax = 0.5

[option]
# tells `3dcorona` to perform geodesic calculations
type = 0

Raytracing parameter file:

[physical]
a = 0.933
m = 10
mdot = 0.72
# corona temperature in kev
te = 100.
# Thomson optical depth; for spherical corona tau = ne * sigma_t * R, where ne
# is the electron density, sigma_t is the Thomson cross section, and R is the
# radius of the corona. For slab, tau = ne * sigma_t * h / 2, where h is the
# thickness of the corona
tau = 1
fcol = 1.7
rin = 1.3

[gridsize]
# number of photons sampled for one geodesic
nphoton = 10000

[option]
# tell `3dcorona_mpi` to perform radiative transfer inside the corona
type = 2
# if the polarized radiative transfer is switched on
pol = 1
# the step size
dr = 0.001
# whether to print the progress
progress = 1
# whether to assume Klein-Nishina cross section
KN = 1
# if chandra = 0, we assume the disc emission is isotropic and is unploarized.
# Otherwise we use the Chandrasekhar's formula (Section X, Chandrasekhar 1960) for a semi-infinite scattering
# atmosphere to determine the disc photon's directionality and polarization angle/degree
chandra = 0
scafile = /scratch2/shashank/4U1630-47/sphere/sca_params.dat
gparamfile = /scratch2/shashank/4U1630-47/sphere/gparams.dat
# Raytracing parameter file is same for all the geometries

Conical case:
parameter 1 file:
[physical]
# black hole spin
a = 0
# the geometry of the corona; 2 for a stationary truncated disc
gtype = 9
# the radius of the corona, in GM/c2
#radius = 30.
# the inner radius of the corona
#corona_rin = 2.
# inner edge of the disc, in GM/c^2; if rin < rms, then rin = rms
rin = 1.22
# outer edge of the disc, in GM/c^2
rout = 1000.
hmin = 2.5
hmax = 10
thickness = 7.5
opening_angle = 25
velocity =0.3

[gridsize]
# number of radial bins on the disc
nr = 100
# number of bins in the polar emission angle of the seed photon
nphi = 100
# number of bins in the azimuthal emission angle of the seed photon
ntheta = 200
# the maximum polar emission angle over PI; 1. means the maximum angle is PI
thetamax = 1.

[option]
# tells `3dcorona` to perform geodesic calculations
type = 0

Slab case:
parameter 1 file:
[physical]
# black hole spin
a = 0
# the geometry of the corona; 1 for a stationary slab; and 5 for a slab
# co-rotating with the disc
gtype = 1
# the minimum height of the corona, in GM/c2
hmin = 3.
# the maximum height of the corona, in GM/c2
hmax = 7.
# radial extent of the corona, in GM/c2
s = 20.
# inner edge of the disc, in GM/c^2; if rin < rms, then rin = rms
rin = 1.22
# outer edge of the disc, in GM/c^2
rout = 1000.

[gridsize]
# number of radial bins on the disc
nr = 100
# number of bins in the polar emission angle of the seed photon
nphi = 100
# number of bins in the azimuthal emission angle of the seed photon
ntheta = 100
# the maximum polar emission angle over PI; 0.5 means the maximum angle is half
# PI
thetamax = 0.5

[option]
# tells `3dcorona` to perform geodesic calculations
type = 0

Wedge case:
Parameter 1 file:
[physical]
# black hole spin
a = 0.933
# the geometry of the corona; 2 for a stationary truncated disc
gtype = 6
# the radius of the corona, in GM/c2
#radius = 30.
# the inner radius of the corona
#corona_rin = 2.
# inner edge of the disc, in GM/c^2; if rin < rms, then rin = rms
rin = 1.22
# outer edge of the disc, in GM/c^2
rout = 1000.
smin = 2.5
smax = 18
maxmu = 0.9063

[gridsize]
# number of radial bins on the disc
nr = 100
# number of bins in the polar emission angle of the seed photon
nphi = 100
# number of bins in the azimuthal emission angle of the seed photon
ntheta = 200
# the maximum polar emission angle over PI; 1. means the maximum angle is PI
thetamax = 1.

[option]
# tells `3dcorona` to perform geodesic calculations
type = 0
