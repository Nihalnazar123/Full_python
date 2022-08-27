# linear search
l=[1,2,3,4,5,6,7,8,0,9,22,44,55,66,87]
e=8
def linear():
    for i in l:
        if i==e:
            print('element found')
            break
    else:
            print('not found')

linear()
