#!/bin/bash
#SBATCH --partition=bch-compute 
#SBATCH --ntasks=1
#SBATCH -t 120:00:00

input=$1
output=$2

echo $input

$SCHRODINGER/utilities/structconvert -imae $input -osd $output
