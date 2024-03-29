
import numpy as np
import math
import operator
import sys
import glob

def main(nmap,energy_range,year):

    nmap=int(nmap) ## nmap =1-100
    energy_range=int(energy_range)##1,2,3
    year=int(year)

    rate=np.load('/beegfs/dampe/users/mmunozsa/ani_random_average/ani_avg_method/rate_ps_year_energybin.npy')
    total_sec=np.load('/beegfs/dampe/users/mmunozsa/ani_random_average/ani_avg_method/total_seconds_peryear.npy')
    total_sec[0]=29540965
    x=rate[year-1,energy_range-1]/total_sec[year-1]
    s = np.random.poisson(x,int(total_sec[year-1]))
    while (s.sum()<rate[year-1,energy_range-1]):
        s = np.random.poisson(x,int(total_sec[year-1]))

    np.save('../pois_dist_year_new_'+str(year)+"_energy_bin"+str(energy_range)+'_nmap_'+str(nmap)+'.npy',s)

if __name__ == '__main__':
        main(sys.argv[1],sys.argv[2],sys.argv[3])
