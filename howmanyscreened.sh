
for file in ShuffledLigands/*; do
    count_mae $file | cat >> how_many_perfile.txt
done
