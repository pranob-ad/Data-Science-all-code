import string
import random

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
digits = string.digits 
spacial_char = string.punctuation
password = string.ascii_letters + digits + spacial_char
#password = list(password)
#print(password)
 
random.sample(password, 8)
password = random.sample(password, 8)

password = ''.join(password)
#print("Password is :", password)


passwd= password
# Check if the password meets the criteria
while len(passwd) < 8:
    print("Password must be at least 8 characters long.")
    passwd = password
    while not any(check in upper_case for check in passwd):
        print("Password must contain at least one uppercase letter.")
        passwd = password
        while not any(check in lower_case for check in passwd):
            print("Password must contain at least one lowercase letter.")
            passwd = password
            while not any(check in digits for check in passwd):
                print("Password must contain at least one digit.")
                passwd = password
                while not any(check in spacial_char for check in passwd):
                    print("Password must contain at least one special character.")
                    passwd = password
                    
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
