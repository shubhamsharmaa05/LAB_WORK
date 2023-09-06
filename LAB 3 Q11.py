##Q11
number = int(input("Enter a 3-digit number: "))
if 100 <= number <= 999:
    A = number // 100
    B = (number // 10) % 10
    C = number % 10
    D = (A ** 3) + (B** 3) + (C** 3)
    if D == number:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
else:
    print("Please enter a valid 3-digit number.")