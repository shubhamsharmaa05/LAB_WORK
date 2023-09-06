##Q7
A=int(input("Enter the no.1"))
B=int(input("Enter the no. 2 "))
C= complex(A,B)
print(C)
D=int(input("Enter the no.1"))
E=int(input("Enter the no. 2 "))
F=complex(D,E)
G=int(input("Enter no. 1 or 2"))
if G == 1 :
    print(complex(A+D,B+E))
if G == 2 :
    print(complex(A*D-B*E,A*E+B*D))
else :
    print("ERROR")