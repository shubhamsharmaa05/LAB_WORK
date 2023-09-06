##Q4
A=int(input("Enter the no on once place"))
B=int(input("Enter the no on ten place"))
C=int(input("Enter the no on hundred place"))
D=(str)(A)+(str)(B)+(str)(C);
print("your no is",D)
if (A+B+C)%3==0:
    print("DIVISIBLE BY 3")
else :
    print("Not divisible by 3")