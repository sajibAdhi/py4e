# Ask for File Name
fname = input("Enter file name: ")

# default file name "mbox-short.txt" if none Given
if len(fname) < 1:
    fname = "mbox-short.txt"

# If File Not Found print it
try:
    # Open the File
    fh = open(fname)

    ddd = dict()

    # Read Lines from File-Handeler
    for line in fh:

        line = line.rstrip()

        if not line.startswith('From'):
            continue
        if line.startswith('From:'):
            continue

        elements = line.split()
        hour = elements[5].split(':')
        key = hour[0]
        ddd[key] = ddd.get(key, 0) + 1

    lst = list()
    for key, value in sorted(ddd.items()):
        print(key, value)

except:
    print('File Not Found')
