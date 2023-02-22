# FUNCTIONS
# ADD DOCSTRING TO FUNCTIONS TO DESCRIBE IT

# IF FUNCTION RETURNS NO VALUE IT IS A 'PROCEDURE'

# 1.
# def output_num(num):
#   """"prints numbers from one to argument"""
#   for x in range(1,num + 1):
#     print(x)
  
# output_num(7)

# 2.
# def odd_or_even(num):
#   """takes one argument and checks if number is even or odd"""  
#   if num % 2 == 0:
#     return print(f"{num} is even")
#   return print(f"{num} is odd")  

# odd_or_even(6)

# 3.
# def multiply(num):
#   """iterates from zero to num and multiplies current element by 9""" 
#   for i in range(0,num + 1):
#     print(i * 9)


# multiply(9)

# 4.
# user_input = int(input('Give me a number: '))

# def multiply_all(num):
#   """prints sum of all numbers from 1 to num"""
#   total = 0
#   for i in range(1, num + 1):
#     total += i
#     print(total)
  
# multiply_all(user_input)


# 5.
# def factorial(num):
#   """prints factorial of a number"""
#   fact_num = 1
#   for i in range(1, num + 1 ):
#     fact_num *= i
#   return fact_num

def factorial(num):
  """recursive example of factorial"""
  if num == 1:
    return 1
  return num * factorial(num - 1)
  
print(factorial(5))


# 6.
# def sentence_change(text):
#   """if text shorter than length of 4 returns text, else returns string of first and last 2 characters"""  
#   new_str = ''
#   if len(text) < 4:
#     return text
#   return new_str + text[0:2] + text[-2:]


# print(sentence_change('computer'))

# 7.
# def remove_odd_chars(text):
#   """returns new string with chars at odd index removed"""
#   new_str = ''
#   for i, char in enumerate(text):
#     if i % 2 != 0:
#       new_str += char
#   return new_str

  

# print(remove_odd_chars('computer'))

# 8.
# def get_first_half(word):
#   """returns string with first half or argument"""
#   new_str = ''
#   for i, char in enumerate(word):
#     if i < int(len(word)/2):
#       new_str += char
#   return new_str
      
   
  
# print(get_first_half('Computer')  )

# 9.
# def insert_word(text, word):
#   """inserts a given into middle of a sentence"""
#   middle = (int(len(text) // 2))
#   new_str = text[:middle] + word + text[middle:]
#   return new_str
  
  
# print(insert_word('Computer','Hi'))  

# 10.
# def remove_substring(word, num1, num2):
#   """returns a string with the part between the indices removed"""
#   new_str = word[0:num1] + word[num2:]
#   return new_str
  

# print(remove_substring('Hello there', 2, 6))


# 11.
# def player1(beans):
#  return beans - 1


# def player2(beans):
#  return beans - 1

# beans = 16


# while beans > 0:
#   beans = player1(beans)
#   if beans == 0:
#     print('player 2 wins!')
  
#   beans = player2(beans)
#   if beans == 0:
#     print('player 1 wins!')