# Task 1: Write a program that prints "Hello, World!" to the console.
print("Hello, World!")

# Task 2: Ask the user for their name using an input prompt. Then, print a personalized greeting using their name.

name = input("What is your name? ")
print('Hello', name)

# Task 3: Ask the user for two numbers. Print the sum, difference, product, and quotient of those two numbers.

user_input1 = input("x = ")
user_input2 = input("y = ")

sum = (int(user_input1) + int(user_input2))
difference = (int(user_input1) - int(user_input2))
product = (int(user_input1) * int(user_input2))
quotient = (int(user_input1) / int(user_input2))
print("Sum = ", sum)
print("difference = ", difference)
print("product = ", product)
print("quotient = ", quotient)

# Task 4: Ask the user for their age. Print out how old they will be next year.

age = input('What is your age? ')
print("Next year, you will be", (int(age) + 1), "years old")
