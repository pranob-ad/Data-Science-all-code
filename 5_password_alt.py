spacial_char = ['$', '@', '#', '%', '&', '!', '^', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

# This code is for password validation
passwd= input("Enter your password: ")
while len(passwd) < 8:
    print("Password must be at least 8 characters long.")
    passwd = input("Enter your password again  : ")
while not any(char.isupper() for char in passwd):
    print("Password must contain at least one uppercase letter.")
    passwd = input("Enter your password again  : ")
while not any(char.islower() for char in passwd):
    print("Password must contain at least one lowercase letter.")
    passwd = input("Enter your password again  : ")
while not any(char.isdigit() for char in passwd):
    print("Password must contain at least one digit.")
    passwd = input("Enter your password again  : ")
while not any(char in spacial_char for char in passwd):
    print("Password must contain at least one special character.")
    passwd = input("Enter your password again  : ")
print("Password is :", passwd)

#lets check the password strength
sum = 0
for check in passwd:
    if check.isupper():
        sum += 1
    elif check.islower():
        sum += 1
    elif check.isdigit():
        sum += 2
    elif check in spacial_char:
        sum += 3

if sum < 10:
    print("password's strength is weak")
elif sum < 17:
    print("password's strength is medium")
else:
    print("password's strength is stong")