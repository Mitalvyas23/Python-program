list = []
length = int(input('enter list length : '))
print('enter elements in list : ')
for i in range(length):
    n = int(input('list[] : '))
    list.append(n)

large = list[i]
for i in range(0,len(list)):
    if(large < list[i]):
        large = list[i]

small = list[i]
for i in range(0,len(list)):
    if(small > list[i]):
        small = list[i]

print('THE LARGEST NUMBER IN LIST IS : ',large)
print('THE SMALLEST NUMBER IN LIST IS : ',small)
