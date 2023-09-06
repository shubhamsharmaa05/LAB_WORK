##Q8 & Q9
A=int(input("Enet the basic salary-"))
B=A/10
C=B+A
D=C/20
E=C+D
F=A/5
G=E+F
print("Total salary",G) 
if G < 300000:
    print("tax is 0%")
elif 300000 <= G < 1000000:
    Z=G/10
    print("TAX is 10%",Z)
elif 1000000 <= G < 2500000:
    X=G/5
    print("TAX is 20%",X)
else:
    Y=(G*3)/10
    print("TAX is 30 %",Y)