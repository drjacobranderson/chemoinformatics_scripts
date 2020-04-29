#!/bin/bash
#SBATCH --partition=bch-compute 
#SBATCH --ntasks=1
#SBATCH -t 120:00:00

directory=PLP_HTVS_confgen_20200428
extension="_pv.sdf"
outputfile=paths_to_sdf_files.txt

find $directory -name "*$extension" > $outputfile

while read line;
do
	cat $line >> 01.PLP_SDF_ALL.sdf

done < $outputfile
