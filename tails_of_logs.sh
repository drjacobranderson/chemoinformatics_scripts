

while read line; do
  tail $line | cat >> HTVS_log_tails.txt
done < log_file_paths.txt
