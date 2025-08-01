#random list
import random
lst = [random.randint(1, 100) for _ in range(10)]

#taking input from user
'''lst = list(input("Enter the list: ").split())
lst = [int(i) for i in lst]
'''

print("List is:", lst)
n = len(lst)
for i in range(0, n):
    for j in range(0, n-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print("Sorted list is:", lst)
if n % 2 == 0:
    midian = (lst[n//2] + lst[n//2 - 1]) / 2
else:
    midian = lst[n//2]
print("Midian is:", midian)



#
mad = 0
mad_lst = [ abs(x - midian) for x in lst]
for i in range(n-1):
    if j in range(n-i-1):
        if mad_lst[j] > mad_lst[j+1]:
            mad_lst[j], mad_lst[j+1] = mad_lst[j+1], mad_lst[j]
print("Sorted mad list is:", mad_lst)

if n % 2 == 0:
    mad = (mad_lst[n//2] + mad_lst[n//2 - 1]) / 2
else:
    mad = mad_lst[n//2]
print("Mad is:", mad)
