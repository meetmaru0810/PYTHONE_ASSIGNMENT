#I3:- : Write a Python program that compute the area of following
#1) Triangle (accepts base and height)2) Circle (accept radius)

#Triangle (accepts base and height)
base=float(input("enter the base of tringle:"))
height=float(input("enter the height of triangle:"))
radius=float(input("enter the radius:"))

T_area=0.5*base*height
C_area=3.14*radius*radius
print("area of tringle=",T_area)
print("area of a circal=",C_area)