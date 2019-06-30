
import numpy as np
import math
import operator
import sys
import glob

def main(nmap,energy_range,year):

nmap=int(nmap) ## nmap =1-100
energy_range=int(energy_range)##1,2,3
year=int(year)

rate=np.load('rate_ps_year_energybin.npy')
total_sec=np.load('total_seconds_peryear.npy')

x=rate[year-1,energy_range-1]/total_sec[year-1]
s = np.random.poisson(x,int(pointing_history[year-1]))
np.save('../pois_dist_year_'+str(year)+"_energy_bin"+str(energy_range)+'_nmap_'+str(nmap)+'.npy')

if __name__ == '__main__':
        main(sys.argv[1],sys.argv[2],sys.argv[3])
