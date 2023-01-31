# from math import pi
# r = 12
# area = pi * r ** 2
# print("The area of a circle with radius", r, "is", area)



# print('What is the secret number')
# my_int = int(input())
# ans = my_int + 2 * 3 - 6 / 3
# print(ans)

# a_int = 7
# b_int = 4
# print(type(a_int % b_int))

# a_int = 10
# b_int = 3
# c_int = 3
# print(b_int ** c_int)

# ... Lab 2

# Q 6

# user_num = int(input('Please give me a number: '))
# print(int(((user_num + 2) * 3 - 6) / 3))

# 7. Assignment:

# my_int = 5
# my_int += 3
# print(my_int)

# 8. Assignment:
# my_var1 = 7.0
# my_var2 = 5
# print(my_var1 % my_var2)

# 9. Prompt for input and then print the input as a string, an integer, and a float-point value. What values can you input and print without errors being generated?

# user_input = input('Give me a number: ')
# print("Here's your value as a string,", str(user_input),",an integer,",int(user_input),",and a float,",float(user_input))

# 10. Consider the expression (a + b) * c , but with string values for a, b, and c. Enter that into the Python shell. What happens? Why?
# Strings must be converted to integers or floats to be added etc


# a = '4'
# b = '6'
# c = '7'
# print((a + b) * c)

# 11. (Integer operators) One way to determine whether an integer is even is to divide the number by 2 and check the remainder. Write a three-line program that prompts for a number, converts the input to an integer, and prints a 0 if the number is even and a 1 if the number is odd.

# user_value = int(input('Please enter a number: '))
# if user_value / 2 == 0:
#   print("Even number!")
# else:
#   print('Odd number!')

# 12. Body mass index (BMI) is a number calculated from a person’s weight and height.
# According to the Centers for Disease Control and Prevention, the BMI is a fairly
# reliable indicator of body fatness for most people. BMI does not measure body fat
# directly, but research has shown that BMI correlates to direct measures of body fat,
# such as underwater weighing and dual-energy X-ray absorptiometry. The formula for BMI is
# weight / height²
# where weight is in kilograms and height in meters.
# (a) Write a program that prompts for metric weight and height and outputs the BMI.
# (b) Write a program that prompts for weight in pounds and height in inches, converts
# # the values to metric, and then calculates the BMI.

# user_weight = int(input("Please enter your weight in kilograms: "))
# user_height = int(input("Please enter your height in cms: "))
# print("Your BMI is", (user_weight / user_height ** 2)* 10000)

user_weight = int(input("Please enter your weight in pounds: "))
user_height = int(input("Please enter your height in inches: "))
print("Your BMI is", (user_weight / user_height ** 2)* 703)