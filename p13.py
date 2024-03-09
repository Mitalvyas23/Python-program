'''Write a python program to count occurrences of an element in a List.'''

list = []
length = int(input('enter list length : '))
print('enter elements in list : ')
for i in range(length):
    n = (input('list[] : '))
    list.append(n)

print(list)
n1 = list.count(input('enter a number to find their occurance in list : '))
print('THE NUMBER OCCURANCE IS : ',n1)

