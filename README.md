Simulation (see in raw)

The corona geometry of the black hole sources are simulated using the Monte Carlo radiative transfer code(Monk). The process that has to be followed is as:

1. The monk code can be downloaded from https://projects.asu.cas.cz/zhang/monk.
2. The system should have the follwoing requirements: 
- GNU Make
- C++ compiler that supports c++14 standard; for GCC starting from GCC 5.0
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
                                                                                  
