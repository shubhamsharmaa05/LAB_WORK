##Q2
A = float(input("Enter your weight(in Pounds)-"))
C = float(input("Enter your Height(in inches)-"))
W = A/0.45
H = C/0.0254
B = 1/H*1/H*W
print(B)
if B < 20 :
    print("UNDER WEIGHT")
elif B > 25 :
    print("OVER WEIGHT")
else :
    print("Normal")