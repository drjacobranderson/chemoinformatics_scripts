
#Set Variables
directory=$1
name=${1::-1}
tmp=pv_paths.txt
merged_file="$name"".mae"
lig_tmp="lig_tmp_$name"".mae"
lig_file="lig_"$name".smi"
r_tmp="tmp_receptor.mae"
receptor="r_"$name".smi"
#Create a path file
find $1 -name "*pv*" >> $tmp

#Use Schrodinger utility to merge the files in the path
$SCHRODINGER/utilities/glide_merge -o $merged_file -f $tmp

#Remove the temporary path file
rm $tmp

$SCHRODINGER/utilities/maesubset -n 2: $merged_file -o $lig_tmp

$SCHRODINGER/utilities/structconvert -imae $lig_tmp -osmi $lig_file

#Remove the .mae ligfile
rm $lig_tmp

$SCHRODINGER/utilities/maesubset -n 1:1 $merged_file -o $r_tmp

$SCHRODINGER/utilities/structconvert -imae $r_tmp -osmi $receptor


#Cleanup all files except the receptor and ligand files
rm $r_tmp
rm $merged_file




