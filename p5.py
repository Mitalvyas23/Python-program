
def my_function(list):
    print('LIST BEFORE SWAP FIRST AND LAST ELEMENT IN LIST : ')
    print(list)
    first = list[0]
    print('first element in list is : ')
    print(first)
    size = len(list)
    last = list[size-1]
    print('last element in list is : ')
    print(last)
    temp = list[0]
    list[0] = list[size-1]
    list[size-1] = temp
    print('LIST AFTER SWAP FIRST AND LAST ELEMENT IN A LIST : ')
    print(list)


my_function([11,22,33,44,55,66,77,88,99])