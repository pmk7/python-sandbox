# keyword def 
# FUNCTIONS
# ADD DOCSTRING TO FUNCTIONS

# IF FUNCTION RETURNS NO VALUE IT IS A 'PROCEDURE'

# def calc(a,b):
#   return a + b
 
# x = calc(5,10)

# new_calc = 20 + x
# print(new_calc)

# VERY IMPORTANT WHERE THE RETURN STATEMENT IS IN EXAMPLE BELOW!

# def generate_evens():
#   num_list = []
#   for num in range(1,50):
#     if num % 2 == 0:
#       num_list.append(num)
#   return num_list


# nice solution using list comprehensions
# def generate_evens():
#     return [x for x in range(1,50) if x%2 == 0]

# print(generate_evens())

# def yell(sentence):
#    return f"{sentence.upper()}!"
  
# print(yell('hi'))

# noises = {
#     "dog": "woof", 
#     "pig": "oink", 
#     "duck": "quack", 
#     "cat": "meow"
# }

# def speak(animal="dog"):
#   noise = noises.get(animal)
#   if noise:
#     return noise
#   return "?"


# print(speak('shoe'))

# def calc(*args):
#   total = 0
#   for num in args:
#     total += num
#   return total
  
# print(calc(1,5,6,7,3))


# def names(**kwargs):
#   for key,val in kwargs.items():
#     print(f"{key}'s fav sport is {val}")
  
  
# names(phil='table tennis')

# def combine_words(**kwargs):
#   if 'prefix' in kwargs and kwargs['word']:
#     return f"{kwargs['prefix']}{kwargs['word']}"
#   elif 'suffix' in kwargs and kwargs['word']:
#     return f"{kwargs['word']}{kwargs['suffix']}"
#   return kwargs['word']
  
# # print(combine_words(word='small'))
# print(combine_words(word='small'))


# PARAMETER ORDERING
# 1. parameters
# 2.*args
# 3. default parameters
# 4. **kwargs

# UNPACKING TUPLES
# def sum_all_values(*args):
#   total = 0
#   for num in args:
#     total += num
#   print(total)

# nums = (5,10,15,20,25)
# # works for list too
# sum_all_values(*nums)

# nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]

# def count_sevens(*args):
#     result = 0
#     for num in args:
#         result += num
#     return result


# print(count_sevens(1,4,7))  
# print(count_sevens(*nums))  

# # ** UNPACKS DICTIONARIES INTO KEY WORD ARGUMENTS  

# def display_names(first,second):
#   print(f"{first} says hello to {second}")

# names = {"first":"Phil", "second":"Ira"}  

# display_names(**names)

def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final

calculate(make_float=False,operation="add",message="you just added",first=2,second=4)