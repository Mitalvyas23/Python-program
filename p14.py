''' Write a python program to multiply all even numbers and odd numbers in 
the List.'''

list = []
length = int(input('enter list length : '))
print('enter elements in list : ')
for i in range(length):
    n = int(input('list[] : '))
    list.append(n)
even = 1
odd = 1
for i in list:
    if i % 2 == 0:
        even = even*i
        #print(even)
    else:
        odd = odd*i
        #print(odd)

print('THE EVEN ELEMENT MULTIPLICATION IS : ',even)
print('THE ODD NUMBER MULTIPLICATION IS : ',odd)
#mul = even*odd
#print(mul)
