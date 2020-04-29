#!/bin/bash
#SBATCH --partition=bch-compute 
#SBATCH --ntasks=1
#SBATCH -t 120:00:00

ligands=$1
receptor=/temp_work/ch216160/3mj5_gridgen_01.pdb


/temp_work/ch216160/rf-score-vs --receptor $receptor $ligands --field "name" --field "RFScoreVS_v2" --field "r_i_docking_score" -O outputfile.csv
