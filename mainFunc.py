import math

def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")


def rectangle_area():
    length = float(input("Please enter the length of the rectangle :"))
    width = float(input("Please enter the width of the rectangle :"))
    area = length * width
    print("The area of the rectangle is :", area)


def circle_area():
    radius = float(input("Please enter the radius of the rectangle :"))
    area = math.pi * (math.pow(radius, 2))
    print("The area of the circle is {:.2f}".format(area))


def main():
    shape_type = input("Get area for what shape: ")
    get_area(shape_type)


main()