def length(list):
    leng = int(input('enter list length : '))
    print('enter elements in list : ')
    for i in range(0,leng):
        n = int(input('list[] : '))
        list.append(n)

    print('your list is : ')
    print(list)
    count = 0
    for i in list:
        count = count+1

    print('LIST LENGTH IS : ',count-1)

length([])