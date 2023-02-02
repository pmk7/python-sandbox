# Loops, if else

# ............


# if between 40 - 60 cigars consumed AND weekday = party successful
# if weekend no upper limit
# 
# a.

# cigars = int(input('number of cigars consumed: '))
# day = input('weekday or weekend?: ')
# if cigars > 40 <= 60 and day == 'weekday':
#     print('True')
# elif cigars > 40 and day == 'weekend':
#     print('True')
# else:
#     print('False')
    
# # b.

# temp = int(input('What is the temperature: '))
# summer = input('is the season summer?: y/n ')

# if temp > 60 and temp <= 90:
#     print('True')
# elif temp > 91 and temp <= 100 and summer == 'y':
#     print('True')
# else:
#     print('False')



# 1. Prompt the user to enter a mark between 0 and 100 and to print “This is a pass” if the mark is 40 or over, and “This is a fail” if the mark is below 40. Hint: use >=

# user_input = int(input('What was your mark? '))
# if user_input < 0 or user_input > 100:
#     print("That's not possible! Try again!")
#     quit()

# if user_input >= 40:
#     print('You passed!')
# else:
#     print('You failed :(')

# 2. Prompt the user to enter two integer numbers, and output if the first is larger, smaller or equal to the second one. Use if-elif-else

# user_input1 = int(input('First number is...? '))
# user_input2 = int(input('And second number is...? '))

# if user_input1 == user_input2:
#     print('Both numbers the same!')
# elif user_input1 > user_input2:
#     print(user_input1, 'is larger')
# else:
#     print(user_input1, 'is smaller')

# 3. Write a small calculator simulator – ask the user to enter two numbers and an operation (+, -, *, /), and either add, subtract, multiply or divide the numbers, and print the result.
    
# user_input1 = float(input('First number is...? '))
# user_input2 = float(input('And second number is...? '))
# user_operator = input('+, -, * or / : ')

# if user_operator != '+' or '-' or '*' or '/':
#     print("That's not a valid operator!")
#     quit()
# if user_operator == '+':
#     print(user_input1 + user_input2)
# elif user_operator == '-':
#     print(user_input1 - user_input2)
# elif user_operator == '*':
#     print(user_input1 * user_input2)
# else:
#     print(user_input1 / user_input2)

#4. Prompt the user for three numbers and print which is the largest of the three.

# user_input1 = float(input('First number is...? '))
# user_input2 = float(input('And second number is...? '))
# user_input3 = float(input('And finally the third number? '))

# if user_input1 == user_input2 and user_input1 == user_input3:
#     print('All the same value!')
# elif user_input1 > user_input2 and user_input1 > user_input3:
#     print(user_input1)
# elif user_input1 > user_input2 and user_input1 < user_input3:
#     print(user_input3)
# elif user_input2 > user_input1 and user_input2 < user_input3:
#     print(user_input3)   
# else:
#     print(user_input2)     


# 5. What output occurs for the following program on the given input?


# user_str = input("Enter a positive integer: ") # Line 1
# my_int = int(user_str)
# count = 0
# while my_int > 0:
#    if my_int % 2 == 1:
#        my_int = my_int//2
#    else:
#        my_int = my_int - 1
#    count += 1 # Line 2
# print(count) # Line 3
# print(my_int) # Line 4

# a. 4
# b. 0
# c. string
# d. increments count by 1 each time 
# e. ensure following suit of code is executed

# 6. How many three-digit numbers are divisible by 17? Write a program to print them.

# num_range = range(100,1000)

# count = 0

# for num in num_range:
#     if num % 17 == 0:
#        count += 1

# print(count)

# 7. Sum of consecutive integers
# (a) Write a program that prompts for an integer — let’s call it X — and then finds the sum of X consecutive integers starting at 1. That is, if X = 5, you will find the sum of 1 + 2 + 3 + 4 + 5 = 15.

# (b) Modify your program by enclosing your loop in another loop so that you can find consecutive sums. For example, if 5 is entered, you will find five sums of consecutive numbers:
# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15


# x = int(input('Give me a number: '))

# num_range = range(0, x + 1)
# ans = 0
# for num in num_range:
#     ans += num
#     print(ans)  



# x = int(input('Give me a number: '))

# ans = 0

# for num in range(1, x + 1):
#     for sin in range(1, num +1):  
#         ans += sin
#     print(ans, sin)
#     ans = 0



X_upper = int(input('Give me a number: '))

for x in range(1, X_upper + 1):
    sum_x = 0
    for i in range(1, x +1):
        sum_x += i
    print("The sum from 1 to ", x, "is", sum_x)
    


 





