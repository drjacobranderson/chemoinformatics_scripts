#!/bin/bash
#SBATCH --partition=bch-compute                           # Partition to run in
#SBATCH --ntasks=1
#SBATCH -t 120:00:00
#SBATCH --output=output_%j.txt          # Name of the output file

echo $1
#Set Variables
directory=$1
name=${1::-1}
tmp=pv_paths.txt
merged_file="$name"".mae"
lig_tmp="lig_tmp_$name"".mae"
lig_file="lig_"$name".sdf"
r_tmp="tmp_receptor.mae"
receptor="r_"$name".sdf"
#Create a path file

find $1 -name "*pv*" >> $tmp

#Use Schrodinger utility to merge the files in the path
echo "Merging the ligands from $tmp"
$SCHRODINGER/utilities/glide_merge -o $merged_file -f $tmp

#Remove the temporary path file
echo "Removing the tmp file storing the poses file postions"
rm $tmp

echo "Extracting the ligands to $lig_tmp"
$SCHRODINGER/utilities/maesubset -n 2: $merged_file -o $lig_tmp

echo "Converting $lig_tmp to $lig_file$"
$SCHRODINGER/utilities/structconvert -imae $lig_tmp -osd $lig_file

#Remove the .mae ligfile
echo "Removing the .mae ligfile"
rm $lig_tmp

echo "Extracting the receptor as mae"
$SCHRODINGER/utilities/maesubset -n 1:1 $merged_file -o $r_tmp
echo "Converting receptor mae to sdf"
$SCHRODINGER/utilities/structconvert -imae $r_tmp -osd $receptor


#Cleanup all files except the receptor and ligand files
echo "Clean-up"
rm $r_tmp
rm $merged_file



