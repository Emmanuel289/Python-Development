# open a file in read mode
file_data = []
for i in range(100):

    f1 = open('/Users/Emmanuel/Desktop/Google drive docs/Professional Development/Python dev/random_file.txt', 'r')

    file_data.append(f1)
    print(i)
    f1.close()  # if we don't close the file each time we open it, we will run out of file handling resources eventually


# open a file in write mode. This deletes content that was previously in an existing file or creates a new file if no
# such file existed previously
f2 = open('/Users/Emmanuel/Desktop/Google drive docs/Professional Development/Python dev/random_file2.txt', 'w')
f2.write('Hello Jupiter!')
f2.close()

# This with keyword allows you to open a file, do operations on it, and automatically close it after the indented
# code is executed, in this case, reading from the file. Now, we don’t have to call f.close()! You can only access
# the file object, f, within this indented block.
with open('/Users/Emmanuel/Desktop/Google drive docs/Professional Development/Python dev/random_file2.txt', 'r') as f:
    file_data = f.read()

