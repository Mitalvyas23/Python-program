'''TOPIC = SWAP ANY TWO ELEMENTS IN LIST 
   PROGRAMMER = Mital vyas'''

def swap(list):
    n1 = int(input('choose one element in a list : '))
    n2 = int(input('choose second element in list : '))
    print('your elements are : ')
    print(n1,n2)
    print('your list before swap : ')
    print(list)

    for i in range(0,len(list)):
        if(n1==list[i]):
            j = i
    
    for i in range(0,len(list)):
        if(n2==list[i]):
            k = i

    temp = list[j]
    list[j] = list[k]
    list[k] = temp
    print('your list after swap : ')
    print(list)

swap([11,22,33,44,55,66,77,88,99])
