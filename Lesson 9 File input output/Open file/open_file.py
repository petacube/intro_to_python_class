with open('input.txt', 'r') as my_file:
    # Some action performed with the file, the read() method explained later.
    print(my_file.read(), '\n')

my_file= open('input.txt', 'r')
# Some action performed with the file, the read() method explained later.
while (line=my_file.read()):
    print(line, '\n')
my_file.close()


with open('input1.txt', 'r') as file:
    print(file.read())


outfile = open('outfile.txt', 'w')  # Opening the file in write mode (using `w` argument)
outfile.write('Hello World')  # Writing to the file, the write() method is explained later.
outfile.close()
