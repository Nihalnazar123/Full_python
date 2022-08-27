f=open('file1.txt', 'r')
for i in f:
    b = open('file2.txt', 'a')
    b.write(i)

