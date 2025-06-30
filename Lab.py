#1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd

num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

#2. Using input function take two number and then swap the number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping: a =", a, "b =", b)

#3. Write a Program to Convert Kilometers to Miles

km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371
print(f"{km} kilometers is equal to {miles} miles")

#4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year. 

P = 200
T = 5
R = 5
SI = (P * T * R) / 100
print("Simple Interest is:", SI)


