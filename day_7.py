#Md Hussain
file = open("C:\\Users\\Ryzen 7 1700\\Downloads\\sample-1.txt", "r")
#or
#file = open(r"C:\Users\Ryzen 7 1700\Downloads\sample-1.txt", "r")
#Prefix the string with r to make it a raw string, which ignores all escape sequences.
contents = file.read()
print(contents)
file.close()

file = open("C:\\Users\\Ryzen 7 1700\\Downloads\\sample-1.txt", "w")
file.write("This is some new content.")
file.close()

file = open("C:\\Users\\Ryzen 7 1700\\Downloads\\sample-1.txt", "w")
file.write("\nThis is some appended content.")
file.close()
