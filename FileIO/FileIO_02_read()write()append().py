# modes:
# append - a
# read - r
# read and write - r+
# write - w

with open('test.txt', mode = 'w') as my_file:
    text = my_file.write('Teeest')
    print(text) # no of characters written
    # no need to close the file

with open('sad.txt', mode = 'w') as my_file1:
    text = my_file1.write(':(')
    print(text)
