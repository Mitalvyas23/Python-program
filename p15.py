''' Write a python program to turn every item of a list into its square'''

list = []
length = int(input('enter list length : '))
print('enter elements in list : ')
for i in range(length):
    n = int(input('list[] : '))
    list.append(n)

print(list)

list1 = []
for i in list:
    list1.append(i*i)

print(list1)
