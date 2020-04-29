ligands=00.eMols_Filtered

destination=PLP_HTVS_confgen_20200428

infile=glide_input_HTVS_PLP.in

mkdir $destination

cp $infile $destination


for file in $ligands/*;do
	echo $file
	./call_glide_all.sh $file $destination $infile $ligands

done

