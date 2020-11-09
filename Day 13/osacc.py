import os
os.chdir("C:\\Users\\Nikhil\\Documents\\Python_Assignments\\Test\\hello")

print(os.getcwd())


print(os.access("test.h", os.W_OK))

print(os.access("test.h", os.R_OK))
