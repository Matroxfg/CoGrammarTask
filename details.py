"""
I will ask the user to write their name, age, house number and street name using the input() function
I will print each input out singularly, so I will create 4 separate print() functions
Finally I will use the f string to put all the inputs together in a string using the inputs as placeholders
I will print it out using the print() function
"""

name = input("Please write your full name here: ")
age = input("Please write your age here: ")
house_number = input("Please write your house number here: ")
street_name = input("Please write your street name here: ")

print(name)
print(age)
print(house_number)
print(street_name)

print(f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name}.")