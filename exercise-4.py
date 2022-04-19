# exercise-04 What kind of Triangle?

print("Please enter the three lengths of a triangle")
length1 = input("length a: ")
length2 = input("length b: ")
length3 = input("length c: ")

if length1 == length2 and length2 == length3:
    print("A triangle with sides of " + length1 + ", " +
          length2 + ", " + length3 + " is an equilateral triangle")

elif length1 != length2 and length1 != length3 and length2 != length3:
    print("A triangle with sides of " + length1 + ", " +
          length2 + ", " + length3 + " is a scalene triangle")

elif length1 == length2 or length2 == length3 or length1 == length3:
    print("A triangle with sides of " + length1 + ", " +
          length2 + ", " + length3 + " is an isosceles triangle")