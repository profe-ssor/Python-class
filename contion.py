 # if and else statements

# if statement = a block of code that will execute if it's condition is true
# else statement = a block of code that will execute if it's condition is false

x = 30
y = 15

x > y

if x > y:
    print("x is greater than y")
else:
    print("x is less than y")

# age = 18

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

x = "red"
y = "blue"
z = "green"

color = "gold"


if color == x:
    print("The color is red.")
elif color == y:
    print("The color is blue.")
elif color == z:
    print("The color is green.")
else:
    print("The color is not recognized.")



password1 = "1234"
confirm_password = "1235"

if password1 == confirm_password:
    print("Password is correct")
else:
    print("Password is incorrect")