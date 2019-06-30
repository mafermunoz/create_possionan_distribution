#!/bin/bash
#SBATCH --partition=rhel6-veryshort
#SBATCH --ntasks=1
#SBATCH --mem=5G
#SBATCH --job-name=Ani


export HOME=/atlas/users/mmunozsa/

source /cvmfs/dampe.cern.ch/rhel6-64/etc/setup.sh
source ~/astro/bin/activate


python poi_dist.py ${1} ${2} ${3} 
