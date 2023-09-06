##Q3
def is_triangle(a, b, c):
   if a + b > c and b + c > a and c + a > b:
     return True
     return False
a = int(input("Enter the length of the first side of the triangle: "))
b = int(input("Enter the length of the second side of the triangle: "))
c = int(input("Enter the length of the third side of the triangle: "))
if is_triangle(a, b, c):
  print("The given numbers can form the sides of a triangle.")
else:
  print("The given numbers cannot form the sides of a triangle.")