ligands=XP_METTL1_NoWater_Ligands

destination=XP_METTL1_NoWater

infile=glide_input_XP_METTL1_NoWater.in


mkdir $destination

cp $infile $destination


for file in $ligands/*;do
	./call_glide_all.sh $file $destination $infile $ligands

done

