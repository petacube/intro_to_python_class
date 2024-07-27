fname = r"C:\Users\stani\work\intro_python2\intro_to_python_class\Lesson 9 File input output\Read file\input.txt"
fname1=r"C:\Users\stani\work\intro_python2\intro_to_python_class\Lesson 9 File input output\Read file\input1.txt"

with open(fname, "r") as f:
    for line in f:
        print(line)


with open(fname1, "r") as f1:
    line=f1.readline()
    line = line.strip()
    print(line)

