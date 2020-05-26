# Use Python to read and write a file

try:
    f = open("myfile.txt", "a")
except:
    print("Error")
else:
    pass

print(f)
writestring = "Hi There"

f.write(writestring)

f.write(writestring)

f = open("myfile.txt", "r")
readvariable = f.read(5)
readvariable = readvariable + ".." + f.read()

print(readvariable)