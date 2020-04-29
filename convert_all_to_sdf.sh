directory=PLP_HTVS_confgen_20200428
extension=".maegz"
outputfile=paths_to_compressed_files.txt

find PLP_HTVS_confgen_20200428 -name "*$extension" > paths_to_compressed_files.txt

while read line;
do
	#Maybe overly verbose way to get the file name without the extension. Will pass for the outputfile name with .sdf appended
	path_for_new_file=${line::-6}".sdf"
	echo $path_for_new_file

	sbatch convert_to_sdf.sbatch $line $path_for_new_file

done < paths_to_compressed_files.txt
