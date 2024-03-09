
''' Write a python program to count and print only unique values from the 
List.
Input = [1, 2, 2, 5, 8, 4, 4, 8]
Output: 
No of unique items are: 5
Unique_list= [1,2,5,8,4]'''

list = []
length = int(input('enter list length : '))
print('enter elements in list : ')
for i in range(length):
    n = int(input('list[] : '))
    list.append(n)

count=0
list1 = []
for i in list:
    if i not in list1:
        count+=1
        list1.append(i)

print('UNIQUE ELEMENTS IN LIST ARE : ',count)
print(list1)
