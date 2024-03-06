list = []
length = int(input('enter list length : '))
print('enter elements in list : ')
for i in range(length):
    n = int(input('list[] : '))
    list.append(n)

count = 0
for i in range(0,len(list)):
    if(list[i] < 0):
        print(list[i])
        count+=1
    
print('NEGATIVE NUMBER IN LIST ARE : ',count)
