#!/bin/bash
#SBATCH --partition=bch-compute                           # Partition to run in
#SBATCH --ntasks=1
#SBATCH -t 120:00:00
#SBATCH --output=output_%j.txt          # Name of the output file

for file in Ligprepafterfilter/*; do
	echo Starting $file cat
	cat $file >> emols_all_as_filt.sdf
	echo $file concatonation finished
done
