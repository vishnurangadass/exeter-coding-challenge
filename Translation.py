import time
import re
import csv
import psutil,os
from csv import reader


#time at the start of program is noted
start = time.time()

with open('french_dictionary.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)


# Read in the file
with open('t8.shakespeare.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
for i in range(1000):
    occurrences = len(re.findall(list_of_rows[i][0],filedata,re.IGNORECASE))
    filedata=re.sub(list_of_rows[i][0],list_of_rows[i][1],filedata,flags=re.I)
    list_of_rows[i].append(occurrences)

# Write the file out again
with open('t8.shakespeare.translated.txt', 'w') as file:
  file.write(filedata)

    
file = open('frequency.csv', 'w+', newline ='')
field = ['English word','French word','Frequency']
with file:	
	write = csv.writer(file)
	write.writerow(field)
	write.writerows(list_of_rows)


#time at the end of program execution is noted
end = time.time()

#total time taken to print the file
process_complete_time = end - start
memory_used = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
with open('performance.txt', 'w') as file:
    file.write(f"Time to process : {process_time} seconds\n")
    file.write(f"Memory used : {memory_used} MB")
print('Done.')
