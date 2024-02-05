# Task #1: Take a user Input(Name, Age, Roll_No, Phone_No and Print the User details
name = input("Enter your Name ")
age = input("Enter your Age ")
roll_number = input("Enter your Roll Number ")
phone_number = input("Enter your Phone Number ")
print("User Details")
print("User Name:", name)
print("User Age:", age)
print("User Roll_Number:", roll_number)
print("User Phone Number:", phone_number)
print("...........................")
# Task #2 - Print the Table of 2 by using the command print()
# 2 x 1 = 2
# 2 x 2 = 4
...
# 2 x 10 = 20
# Use printf command

num = int(input("Enter a number:"))
print("Table of:")
for a in range(1,11):
    print(num,'x',a,'=',num*a)