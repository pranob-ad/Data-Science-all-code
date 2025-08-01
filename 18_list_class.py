class My_list:
    def __init__(self, initial_list):
        self.data = initial_list

    def set_second_entry(self, value):
        self.data[1] = value


    def append_value(self, *values):
        self.data.extend(values)

    def remove_value(self):
        self.data.pop(0)

    def sort(self):
        self.data.sort()

    def double_list(self):
        self.data = self.data * 2 # or self.data += self.data or self.data.extend(self.data)

    def insert_at_index(self, index, value):
        self.data.insert(index, value)

    def __str__(self):
        return str(self.data)
    
#Create a My_list object with an initial list
my_list = My_list([1, 2, 3, 4, 5])

#perform operations on the list
my_list.set_second_entry(17)
my_list.append_value(4,5,6)
my_list.remove_value()
my_list.sort()
my_list.double_list()
my_list.insert_at_index(2, 35)

# Print the final state of the list
print(my_list)  # Output: [2, 3, 99, 4, 5, 6, 7, 8, 2, 3, 99, 4, 5, 6, 7, 8]