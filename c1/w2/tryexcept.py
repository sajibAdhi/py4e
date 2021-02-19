str = input('Write Anything: ')

try:
    str = int(str)
except:
    str = -1

print('First ', str)

inte = input('Write Anything Integer: ')

try:
    print('Hello ')
    inte = int(inte)
except:
    inte = -1

print('Second ', inte)