directory=PLP_HTVS_confgen_20200428
extension="_pv.sdf"
outputfile=paths_to_sdf_files.txt

find $directory -name "*$extension" > $outputfile

while read line;
do
	#Maybe overly verbose way to get the file name without the extension. Will pass for the outputfile name with .sdf appended
	#path_for_new_file=${line::-6}".sdf"
	echo $line
	sbatch send-rf.sbatch $line


done < $outputfile
