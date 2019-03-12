infile = open('1950_readable.txt')
metadata = infile.read()
metadata_list = metadata.split("\n")

for line in metadata_list:
    if "Period:" in line:
        print(line[8:])

for line in metadata_list:
    if "Primary Subject Author: " in line:
        print(line[24: ])

for line in metadata_list:
    if "Primary Subject Work:" in line:
        print(line[22:])

#This is a case in which some values have multiple fields separated by semicolons! I'm writing some code to try to get it to print out in a copyable fashion, but it's not working for me yet.
classification_list_1950 = []
for line in metadata_list:
    if "Classification: " in line:
        print(line[16:])
        classification_list_1950.append(line[16:])

#for example, this. But it doesn't really help.
separated_list_1950 = []
for line in classification_list_1950:
    print(line.split(";"))

#this doesn't work and it's weird
for line in metadata_list:
    if "Subject Terms" in line:
        label_line = metadata_list.index(line)
        print(metadata_list[label_line + 1])
    else:
        pass

infile.close()