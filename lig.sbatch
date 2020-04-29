#!/bin/bash
#SBATCH --partition=bch-compute 
#SBATCH --ntasks=%NPROC% 
#SBATCH -t 120:00:00

./ligprep.sh
