import random

class ArrayOperation:
    def __init__(self, size):
        self.A = [random.uniform(-1,1) for _ in range(size)]
        self.B = [random.uniform(-1,1) for _ in range(size)]
    
    def inner_product(self):
        product = 0
        for i in range(len(self.A)):
            product += self.A[i] * self.B[i]
        return product
        
class ArrayShifter(ArrayOperation):
    def __init__(self, size):
        super().__init__(size) #initialize the base class

    def circular_shift(self):
        temp = self.B[0]
        for i in range(len(self.B)-1):
            self.B[i] = self.B[i+1]
        self.B[-1] = temp

#create an ArrayShifter object
shifter = ArrayShifter(5)

#print the initial arrays
print("Array A:", shifter.A)
print("Array B:", shifter.B)

#perform inner product
for i in range(5):
    shifter.circular_shift()
    inner_prod = shifter.inner_product() #useing shifter instead of shifet
    print(f"shift {i+1}: Inner product = {inner_prod:.2f}")
    # or print("shift " + str(i+1) + ": Inner product = " + str(inner_prod))