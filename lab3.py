# more loops and conditionals

# .......



# int_str = input("Please give me an integer:")
# first_int = int(int_str)
# int_str = input("Please give me a second integer:")
# second_int = int(int_str)

# # print(first_int, second_int)

# tens_count = 0
# loop_count = 0


# while first_int > 10 and second_int < 20:
#    if first_int == 10 or second_int == 10:
#        tens_count += 1
#    first_int -= 5
#    second_int += 5
#    loop_count += 1
  
# print(tens_count) # Line 1
# print(loop_count) # Line 2
# print(first_int) # Line 3
# print(second_int) # Line 4




# (a) Given user input of 20 followed by an input of 10, what value is output by:
# i. Line 1 of the program?
# ii. Line 2 of the program?
# iii. Line 3 of the program?
# iv. Line 4 of the program?
# (b) Given user input of 20 followed by an input of 20, what value is output by:
# i. Line 1 of the program?
# ii. Line 2 of the program?
# iii. Line 3 of the program?
# iv. Line 4 of the program?
# (c) What input will cause both first int and second int to be equal to 10
# at the end of the program?





# import random

# secret_num = random.randint(1,10)
# user = int(input('Guess a number between 1 and 10: '))

# count = 0
# while user != secret_num and count < 10:
#   count += 1
#   print('You have', 10 - count, 'guesses remaining')
#   user = int(input('Try again! '))
# else:
#   print('You won!')
#   user = int(input('Guess a number between 1 and 10: '))


# 2. Write a FOR loop that will iterate from 0 to 20. For each iteration, it will check if the current number is even or odd, and report that to the screen (e.g. "1 is odd, 2 is even").

# for x in range(21):
#   if x % 2 == 1:
#     print(x, "is odd")
#   else:
#     print(x, "is even")

# 3. (a) Write a FOR loop that will iterate from 0 to 10. For each iteration of the loop, it will multiply the number by 9 and print the result (e.g. "2 * 9 = 18").
# (b) Use a nested loop to show the tables for every multiplier from 1 to 10 (100 results total).

# for num in range(11):
#   result = num * 9
#   print("Result of ", num, "* 9", "equals", result)


for num in range(1,11):
  for i in range(1,11):
    result = num * i
    print("Here's the tables multiplier of", num, "by", i, ": and the result", result)
  print('........')

# 4. Write a program to calculate and print the factorial of a number using a FOR loop. The factorial of a number is the product of all integers up to and including that number, so the factorial of 4 is 4*3*2*1= 24


# user_input = int(input('Give me a number and I will return the factorial: '))

# factorial = 1

# for num in range(1, user_input + 1):
#     factorial *= num
   

# print("The factorial of", user_input, "is", factorial)

# 5. What output occurs for the following program on the given input?


# number_str = input("Enter an int: ")
# number = int(number_str)
# count = 0


# while number > 0:
#    if number % 2 == 0:
#        number = number // 2
#    elif number % 3 == 0:
#        number = number // 3
#    else:  # Line 1
#        number = number - 1  # Line 2
#    count = count + 1


# print("Count is: ", count)  # Line 3
# print("Number is: ", number)  # Line 4


# (a) Given user input of 9, what value does Line 3 of the program print?
# (b) Given user input of 9, what value does Line 4 of the program print?
# (c) Given user input of 7, what value does Line 3 of the program print?
# (d) Given user input of 1, what value does Line 3 of the program print?
# (e) If the else clause on Line 1 and Line 2 were removed, what effect would
# that have on the program with the input value 1?
# i. No effect; the program would give the same results.
# ii. The count would be larger.
# iii. The count would be smaller.
# iv. The while loop would not end.
# v. None of the above.

# 6. Ask the user to enter a number and print it back on the screen. Keep asking for a new number until they enter a negative number.


# user_input = int(input('Give me a number: '))
# count = 0
# while user_input > 0 and count < 20:
#   if user_input > 1:
#     count += 1
#     user_input = int(input('Try again! '))
#   else:
#         print('Congrats! We can all go home! ')
#         break
    
  
char = '*'

user_input = int(input('Give me a number: '))

for num in range(1, user_input + 1 ):
  print(char * num)