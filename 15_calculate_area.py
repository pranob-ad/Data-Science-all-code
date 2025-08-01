def cal_area(shape, *dim):
    if shape == "circle":
        print(dim)
        radius, = dim #the "," is imp, bcz it is a tuple so it has by default. one element, so we have to unpack it.
        return 3.1415 * radius ** 2
    elif shape == "rectangle":
        print(dim)
        length, width = dim
        return length * width
    elif shape == "triangle":
        print(dim)
        base, height = dim
        return 0.5 * base * height
    else:
        return "Invalid shape. Please enter circle, rectangle, or triangle."
    return 0

#taking input from the user
shape = input("Enter the shape (circle/rectangle/triangle): ").lower()
'''
The .lower() method is used to convert the user's input to lowercase. 
if the user types it (e.g., "Circle", "CIRCLE", or "circle" will all be treated 
the same). This makes the input handling case-insensitive and more user-friendly.
'''

if shape == "circle":
    radius = float(input("Enter the radius: "))
    area = cal_area("circle", radius)
elif shape == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = cal_area("rectangle", length, width)
elif shape == "triangle":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = cal_area("triangle", base, height)
else:
    area = "Invalid shape. Please enter circle, rectangle, or triangle."

print("Area is:", area)
'''
circle_area = cal_area("circle", 7)
print("Area of circle is:", circle_area)
recatangle_area = cal_area("rectangle", 5, 10)
print("Area of rectangle is:", recatangle_area)
triangle_area = cal_area("tringle", 5, 10)
print("Area of triangle is:", triangle_area)
'''