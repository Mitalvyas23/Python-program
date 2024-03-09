''' Write a menu driven program to perform the following task:
1. Reverse all strings in string List.
2. Convert all elements to upper case
3. Sort the elements of list'''

print('WELCOME TO PERFORM MENU DRIVEN PROGRAM : ')
print('1 : revrse all string in string list')
print('2 : convert all elements in to uppercase')
print('3 : sort all elements in list')
print('4 : exit')
choice = int(input('enter your choice : '))

match choice:
    case 1:
        list = []
        length = int(input('enter list length : '))
        print('enter elements in list : ')
        for i in range(length):
            n = (input('list[] : '))
            list.append(n)

        print('THE LIST BEFORE REVERSE : ')
        print(list)
        print('THE REVERSE LIST IS : ')
        list.reverse()
        print(list)
    case 2:
        list = []
        length = int(input('enter list length : '))
        print('enter elements in list : ')
        for i in range(length):
            n = (input('list[] : '))
            list.append(n)

        list1 = []
        print('THE UPPERCASE LIST IS : ')
        for i in list:
            i = i.upper()
            list1.append(i)

        print(list1)
    case 3:
        list = []
        length = int(input('enter list length : '))
        print('enter elements in list : ')
        for i in range(length):
            n = (input('list[] : '))
            list.append(n)

        list.sort()
        print(list)
    case 4:
        print('please enter valid number')

