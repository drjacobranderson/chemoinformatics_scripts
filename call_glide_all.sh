#!/bin/bash

file=$1
destination=$2
infile=$3
ligands=$4

name="${file##*/}"
attach=$(echo $file | sed 's/^\..\///')
name="${name%.*}"


cd $destination

mkdir $name

cp $infile $name

echo LIGANDFILE "../../"$attach>> $name/$infile

cd $name
mv $infile $name'_'$destination'.in'

$SCHRODINGER/glide $name'_'$destination'.in' -HOST schrodinger -NJOBS 1 -OVERWRITE

cd ..
