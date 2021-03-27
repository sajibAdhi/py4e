fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)

for line in fh:
    string = line.rstrip()
    
count = 0

print("There were", count, "lines in the file with From as the first word")
