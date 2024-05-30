import numpy as np
import matplotlib.pyplot as plt

bin = ['2-3.5','3.5-5','5-6.5','6.5-8']

#function to read and extract the polarization file
def pol_deg(geometry,specification,list_name):

  for i in bin:
    path_deg = np.fromfile('/content/drive/MyDrive/simulation_try/4U1630-47' + geometry + specification + i + '/poldeg.dat')
    if path_deg not in list_name:
            list_name.append(path_deg)

def pol_ang(geometry,specification,list_name):

  for i in bin:
    path_ang = np.fromfile('/content/drive/MyDrive/simulation_try/4U1630-47' + geometry + specification + i + '/polang.dat')
    if path_ang not in list_name:
            list_name.append(path_ang)


def get_list_name(lst):
    for name, value in globals().items():
        if value is lst:
            return name
    return None
marker = ['o','^','s','P']
empty = [np.nan,np.nan,np.nan,np.nan]
label2 = ['slab geometry','spherical geometry','conical geomtery']
label3 = ['velocity 0','velocity 0.3','velocity 0.5']
label4 = ['opening_angle 20','opening_angle 30','opening_angle 40']
label5 = ['case 1','case 2','case 3','case 4']

#function to 
def plot(deg_list, ang_list, r_lim, theta_max, theta_min,label_name):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    for i in range(len(deg_list)):

      r = [deg_list[i][0],deg_list[i][0],deg_list[i][0],deg_list[i][0]]
      theta = np.degrees(ang_list[i][0],ang_list[i][0],ang_list[i][0],ang_list[i][0])

      color = ['blue', 'red', 'green', 'violet']
      label1 = ['2-8 kev']

      for m in range(len(r)):
        if i == 0:
          plt.polar(np.radians(theta[m]), r[m], marker=marker[i],markersize=8, linestyle='', color='blue',label = label1[m])
        else:
          plt.polar(np.radians(theta[m]), r[m], marker=marker[i],markersize=8, linestyle='', color=color[m])
    for i, label in enumerate(label_name):
        plt.polar(np.radians(empty[i]), empty[i], marker=marker[i], linestyle='', color='blue', label=label)
    plt.ylim(0, r_lim)
    ax.set_thetamin(theta_min)
    ax.set_thetamax(theta_max)

    plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1))
    list_name_var = get_list_name(deg_list)
    #plt.title('Polar Plot of Pol_deg vs Pol_ang for ' + list_name_var + ' geometry')
    plt.show()

#Example of a case for spherical geometry  
sph_deg_100_ws = []
sph_deg_100_sam = []
sph_deg_100_geet = []
sph_ang_100_ws = []
sph_ang_100_sam = []
sph_ang_100_geet = []

#read polarization files
pol_deg('4U1630-47/','/spherical','/sph2/kt100_ws/pol/',sph_deg_100_ws)
pol_ang('4U1630-47/','/spherical','/sph2/kt100_ws/pol/',sph_ang_100_ws)

pol_deg('4U1630-47/','/spherical','/sph2/kt100_sam/pol/',sph_deg_100_sam)
pol_ang('4U1630-47/','/spherical','/sph2/kt100_sam/pol/',sph_ang_100_sam)

pol_deg('4U1630-47/','/spherical','/sph2/kt100_geet/pol/',sph_deg_100_geet)
pol_ang('4U1630-47/','/spherical','/sph2/kt100_geet/pol/',sph_ang_100_geet)

sph_deg_kt100 = [sph_deg_100_ws,sph_deg_100_sam,sph_deg_100_geet]
sph_ang_kt100 = [sph_ang_100_ws,sph_ang_100_sam,sph_ang_100_geet]

#Plotting the polarization parameters
plot(sph_deg_kt100,sph_ang_kt100,0.04,10,90,label5)






