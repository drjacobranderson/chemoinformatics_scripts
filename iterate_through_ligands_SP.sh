ligands=SP_METTL1_Ligands

destination=SP_METTL1_NOWater

infile=glide_input_SP_METTL1_Nowater.in


mkdir $destination

cp $infile $destination


for file in $ligands/*;do
	./call_glide_all.sh $file $destination $infile $ligands

done

