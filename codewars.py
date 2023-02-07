# def invert(lst):
#   return [-x for x in lst]

# print(invert([1,0,7,3,4,-5]))

# MY SOLUTION
# def digitize(n):
#   num_lst = list(filter(lambda i: (i),str(n)))
#   res = num_lst[::-1]
#   return [int(item) for item in res]

# # CLEANER SOLUTION
# def digitize(n):
#     return map(int, str(n)[::-1])  
  
# print(digitize(32456))
# print(digitize(0))


# nums = [1,3,4,5,6,7,8]
# print(nums[::-1])

# haystack = ['3', '123124234', None, 'needle', 'world', 'hay']

# def find_needle(haystack):
#   index = 0
#   for item in haystack:
#     if item == 'needle':
#       return f"{item} found at index of {index}"
#     index += 1

# CLEANER SOLUTION
# def find_needle(haystack):
#   return haystack.index('needle')

# print(find_needle(haystack))

my_str = 'hi'
my_str.

def remove_char(s):
  return s[1:-1]
  
print(remove_char('hello'))