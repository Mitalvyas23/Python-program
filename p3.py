list = []
length = int(input('enter list length : '))
print('enter elements in list : ')
for i in range(length):
    n = int(input('list[] : '))
    list.append(n)

print('list is : ')
print(list)
sum = 0
for i in list:
    sum += i

avg = sum/length
print('LIST SUM IS : ',sum)
print('LIST AVERAGE IS : ',avg)