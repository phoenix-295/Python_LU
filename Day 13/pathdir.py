import os
os.chdir("C:\\Users\\Nikhil\\Documents\\Python_Assignments\\Test\\")

print(os.path.isdir("hello"))


def fun1():
    fr = open("file.txt", "w")
    fr.write("Hello")
    fr.close()


print(os.path.isdir("Hello"))
if(os.path.isdir("hello")):
    fun1("hello")
else:
    os.mkdir("Hello")
