# Ask for File Name
fname = input("Enter file name: ")

#default file name "mbox-short.txt" if none Given
if len(fname) < 1:
    fname = "mbox-short.txt"

#If File Not Found print it
try:
    #Open the File
    fh = open(fname)
    
    ddd = dict()
    
    #Read Lines from File-Handeler
    for line in fh:

        line = line.rstrip()

        if not line.startswith('From'):
            continue
        if line.startswith('From:'):
            continue

        elements = line.split()
        key = elements[1]

        ddd[key] = ddd.get(key, 0) + 1

    maxMailSender = None
    maxMailSenderNum = None

    for key,value in ddd.items():
        if maxMailSenderNum is None or value > maxMailSenderNum:
            maxMailSenderNum = value
            maxMailSender = key

    print(maxMailSender, maxMailSenderNum)

except:
    print('File Not Found')