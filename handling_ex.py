try:
    r = float(input("what is the radius? \n"))
    print("the surface of the circle is", r**2*3.14159265)
except ValueError:
    print("Data viitoare sa dai un numar corect")
