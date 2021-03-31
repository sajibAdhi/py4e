import re

fh = open('regex_sum_1171061.txt')
number = 0
count = 0
for line in fh:
    for str in re.findall('([0-9]+)',  line):
        number = number + int(str)
        count = count + 1
print('There are ', count, 'values with a sum=', number)
