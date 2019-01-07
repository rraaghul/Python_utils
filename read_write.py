### Code to read write files ####


### read using csv reader
import csv
file_name = ''
with open(file_name, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for lines in csv_reader:
        print(lines)

### write using csv writer
import csv
df_list = []
with open('submisson.csv','w') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerows(df_list)

### read txt file
with open('input.txt','r') as f:
    output = f.read()

### write to txt file
with open('output.txt', 'w') as file: 
    file.write('')
