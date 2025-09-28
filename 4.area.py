def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius

    return area
val_radius = float(input("Enter radius: "))
circle = area_of_circle(val_radius)
print(f"Area of the circle is {circle}")