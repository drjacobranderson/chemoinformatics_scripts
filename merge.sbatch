#!/bin/bash
#SBATCH --partition=bch-compute 
#SBATCH --ntasks=1 
#SBATCH -t 120:00:00

$SCHRODINGER/utilities/glide_merge -o 01_PLP_HTVS_Alldocked.maegz -f paths_to_compressed_files.txt
