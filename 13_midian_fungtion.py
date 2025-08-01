import random
def sort_list(lst): 
    """This is a funtion of sorting the list, the random input is to be storted
      as a ascending order.
    """
    n= len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

#random list
lst = [random.randint(1, 100) for _ in range(10)]
print("List is:", lst)

#calling the sort_list function and sorted as a ascending order
midian = sort_list(lst)
print("Sorted list is:", midian)

def midian_calc(lst): # this is a function of calculating the midian
    n = len(lst)
    if n% 2 == 0:
        midian = (lst[n//2] + lst[n//2 - 1]) / 2
    else:
        midian = lst[n//2]

    return midian

#calling the midian_calc function and calculating the midian
median = midian_calc(midian)
print("Midian is:", median)

#calculating the absolute deviation
mad_lst= [abs(x - median) for x in lst]
sorted_mad_lst = sort_list(mad_lst)
print("Sorted mad list is:", sorted_mad_lst)

mad = midian_calc(sorted_mad_lst)
print("Mad is:", mad)
