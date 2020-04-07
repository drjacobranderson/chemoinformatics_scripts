import time

start = time.time()

c=0
name_list = []

#Titles of text blocks I want to extract
with open('top10p_of_rfvs_dupsremoved.txt','r') as names:
	for name in names:
		name_list.append(name.strip())
name_list = set(name_list)

#Writing the text blocks to this file
with open("my_python_subset.sdf",'w') as subset:
    
    #Opening the large file with many textblocks I don't want
	with open("noreceptor_3clprot_ALL.sdf",'r') as f:
        
        #Loop through each line in the file
		for line in f:
            
            #Avoids appending extreanous lines or choking 
			if line.split() == []:
				continue
            
            #The lines I want to compare to the name_list has characteristics I added here
            #so that if it doesn't match these quick conditionals it will move on
			if ("-" not in line.split()[0]) and (len(line.split()[0]) >= 5) and (line.split()[0] in name_list):
				c=1 #when c=1 it designates that line should be written
				print("Match ",line)
				name_list.remove(line.strip())


            #Stop writing to file once we see "$$$$"
			if c==1 and line.split()[0] == "$$$$":
				c=0
				subset.write(line)
                
			#Write this line to output file
			if c==1:
				subset.write(line)
            
                

                
stop = time.time()

print("Complete!")
print(stop-start)
