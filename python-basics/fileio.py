# Name: Valentine Kimani
# Date: 24/02/2026
# Program to show file handling  in python


#create new file 
import os


new_file = open("newfile.txt", "r+")

#write to new file
new_file.write("student name: Valentine Kimani ,ID:22202666 , email:valentinekimani4@gmail.com,course:Finance ")
new_file.close()


#read from file
new_file = open("newfile.txt", "r")
data=new_file.read()
print(data)
new_file.close()

#delete file
#import os
os.remove("remove.txt")




#delete folder