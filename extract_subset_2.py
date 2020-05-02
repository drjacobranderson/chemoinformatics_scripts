#!/usr/bin/env python
# coding: utf-8

name_file="names_only.txt"
file_to_extract_from="01.XP_METTL1.sdf"
output_file_name="receptor_removed.sdf"


import time

start = time.time()

c=0
name_list = []

#Titles of text blocks I want to extract
with open(name_file,'r') as names:
	for name in names:
		name_list.append(name.strip())
name_list = set(name_list)

#Writing the text blocks to this file
with open(output_file_name,'w') as subset:
    
        #Opening the large file with many textblocks I don't want
        with open(file_to_extract_from,'r') as f:

            #Loop through each line in the file
            for line in f:
                split=line.split()

                #Avoids appending extreanous lines or choking 
                if split == []:
                    if c == 1:
                        subset.write(line)
                    continue

                #The lines I want to compare to the name_list has characteristics I added here
                #so that if it doesn't match these quick conditionals it will move on
                if ("-" not in split[0]) and (len(split[0]) >= 5) and (split[0] in name_list):
                    c=1 #when c=1 it designates that line should be written
                    print("Match ",line)
                    name_list.remove(line.strip())


                #Stop writing to file once we see "$$$$"
                if c==1 and split[0] == "$$$$":
                    c=0
                    subset.write(line)

                #Write this line to output file
                if c==1:
                    subset.write(line)
            
                

                
stop = time.time()

print("Complete!")
print(stop-start)


