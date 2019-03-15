infile = open('txt' + '/' + '1980_readable.txt')
metadata = infile.read()
metadata_list = metadata.split("\n")

for line in metadata_list:
    #print(line)
    if "Subject" in line:
        print(line)
        label_line = metadata_list.index(line)
        print(label_line)
        print(metadata_list[label_line + 1])

infile.close()