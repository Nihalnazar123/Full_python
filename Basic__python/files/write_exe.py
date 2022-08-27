# write (how to add data to a txt file)
# write function will replace the old data upon writing new data
f=open('datawrite.txt', 'w')
f.write('hello \nhi'
        '\nluminar'
        '\ntechnolab')

# if we use a invalid file name to write data it will automatically create a file with that name and write data
f=open('datanewappend.txt', 'w')
f.write('hello \nhi')
