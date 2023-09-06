##Q10
A = float(input("Enter the first number: "))
B = float(input("Enter the second number: "))
C = float(input("Enter the third number: "))
if A >= B:
    if A >= C:
        L = A
    else:
        L = C
else:
    if B >= C:
        L = B
    else:
        L = C
print(f"The largest number is:",L)