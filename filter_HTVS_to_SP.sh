echo "What precision level"
read precision
echo "What cutoff"
read cutoff
textfilename=$precision"_filepaths.txt"
ofile="filtered_"$precision.maegz 

find $1 -name "*.maegz" > $textfilename

$SCHRODINGER/utilities/glide_merge -o $ofile -c $cutoff -f $texfilename


 
