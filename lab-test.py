# LAB TEST
# REMEMBER DOCSTRING


def sum_digits_squared(number):
  """returns sum of squared digits"""
  str_num = str(number)
  answer = 0
  for num in str_num:
    answer += int(num) ** 2
  return answer

# print(sum_digits_squared(23))


def check_happy_numbers(num):
  """returns true if argument is happy number, returns false if argument is unhappy number, otherwise recursively calls itself"""
  # calling sum_digits_squared function to check if num is happy or not
  if sum_digits_squared(num) == 1:
  # if happy number return True
    return True
  elif sum_digits_squared(num) == 4:
  # if unhappy number return False
    return False
  else:
  # recursively checking if num is happy number, breaking problem into smaller pieces using recursion
   ans = sum_digits_squared(num)
  #  print(ans)
   return check_happy_numbers(ans)


def show_all_happy_numbers(n):
  """prints all happy numbers in range of 1 - n, else prints message that n is not a happy number"""
  # storing all happy numbers as a string
  happy_num_sequence = ''

  if check_happy_numbers(n):
  # calling check_happy_numbers function to check
  # if it return True, we loop over every number from to n
  
    for element in range(1,n):
      if check_happy_numbers(element):
        # checking if individual element in range is a happy number. If yes, we concatenate that element to the happy_num_sequence
        happy_num_sequence += str(element) + ' '
    print(f"All happy numbers up to {n} are:\n{happy_num_sequence}{n}")
    else:
    print("This is not happy number")
  
  
user_input = (int(input("Please enter a number: ")))    
show_all_happy_numbers(user_input)
