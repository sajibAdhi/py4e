fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    str = line.strip().split()
    for single in str:
        if single in lst:
            continue
        else:
            lst.append(single)
lst.sort()
print(lst)
