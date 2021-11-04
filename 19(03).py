dog_years = float(input("Enter dog's age in human years: "))

if dog_years == 1:
    a = 10.5
    print(f"The dog's age in dog's years is {a} years.")
elif dog_years == 2:
    a = 21
    print(f"The dog's age in dog's years is {a} years.")
elif dog_years >= 3:
    b = 21 + (dog_years - 2) * 4
print(f"The dog's age in dog's years is {int(b)} years.")