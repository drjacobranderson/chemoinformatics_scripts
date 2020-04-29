cd Ligprepafterfilter

for file in *; do
        echo $file
        name="${file##*/}"
        attach=$(echo $file | sed 's/^\..\///')
        name="${name%.*}"
        echo $name

        $SCHRODINGER/ligprep -s 1 -i 2 -W i,-ph,7.0,-pht,0.0 -t 1 -HOST schrodinger -NJOBS 1 -ismi $file -osd $name"_ligp.sdf"
done
