file = open("my_file.txt", "w")

file.write("Hi! this is a python file\n")
contant = input("enter the content: ")

file.write(contant)

file = open("my_file.txt", "r")
print(file.read())

file = open("my_file.txt", "a")
enter = input("enter the content: ")
file.write(enter)
file.close()
