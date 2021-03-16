# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
totalValue = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count = count+1
    startPos = line.find(':')
    value = line[startPos+1:]
    value = float(value)
    totalValue = totalValue + value
avg = totalValue/count
print("Average spam confidence:", avg)
