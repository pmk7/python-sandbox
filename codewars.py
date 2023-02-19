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

# my_str = 'hi'
# my_str.

# def remove_char(s):
#   return s[1:-1]
  
# print(remove_char('hello'))

# def high_and_low(numbers):
# """Returns hightest and lower in a string of numbers"""
#   highest = 0
#   lowest = 5
#   arr = numbers.split()
#   num_list = []
#   for x in arr:
#     num_list.append(int(x))
    
#   for el in num_list:
#     if el > highest:
#       highest = el
 
        
#   for el in num_list:
#     if el < lowest:
#       lowest = el
  
  
#   return f"{highest} {lowest}"

    
      
      
# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")) 


# def find_uniq(arr):
  # unique_nums = set()
  # repeated_nums = set()
  
  # for num in arr:
  #   if num in unique_nums:
  #     unique_nums.remove(num)
  #     repeated_nums.add(num)
  #   elif num not in repeated_nums:
  #     unique_nums.add(num)
  
  #   if len(unique_nums) == 1:
  #     return print(unique_nums.pop())
  #   else:
  #     return None

# def find_uniq(arr):
#   unique = arr[0]

#   if arr[0] == arr[1]:
#     for i in range(2, len(arr)):
#       if arr[i] != arr[0]:
#         unique = arr[i]
#         break
#       else:
#         unique = arr[1] if arr[1] != arr[2] else arr[0]
#     return print(float(unique))
  
  
  
  
  
# # find_uniq([0, 0, 0.55, 0, 0])  
# find_uniq([1,1,1,1,1,3])  
  
  
  
  
  # counter = 1
  # unique = arr[0]
  # second = arr[1 + counter]
  # third = arr[2 + counter]
  # temp = arr[counter]
  
  # for i,x in enumerate(arr):
  #   if x != temp or x != second or x != third:
  #     # print(x)
  #     unique = x
  #     counter += 1
  # print(float(unique))
    
  
  # unique = []
  # ans = []    
  
  # for el in arr:
  #   if el not in unique:
  #     unique.append(el)
  
  # for i in unique:
  #   if i in arr:
  #     unique.pop(i)
  #     return unique
    
    
# def solution(s):
#   if len(s) % 2 == 1:
#     new_str = s + '_'
#   else:
#     new_str = s
  
#   pairs = [new_str[i:i+2] for i in range(0, len(new_str), 2)]
#   return pairs
    
    
# print(solution('abcde'))    


# def move_zeros(lst):
#   zeros = []
#   ans = []
#   for x in lst:
#     if x != 0:
#       ans.append(x)
#     else:
#       zeros.append(x)
#   return ans + zeros  
  
  
# print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))


# def order(sentence):
#     words = sentence.split()
#     sorted_words = [""] * len(words)
#     for word in words:
#         for char in word:
#             if char.isdigit():
#                 sorted_words[int(char) - 1] = word
#                 break
#     return " ".join(sorted_words)
    

# print(order("is2 Thi1s T4est 3a"))

# def duplicate_count(text):
#   counter = 0
#   ans_str = ''
#   for i, el in enumerate(text):
#     if el == text[i]
#   print(counter)
    
  
  
  
# duplicate_count("aabbcde")


def camel_case(string):
  # ans = ''.join([x.capitalize() for x in string.split()])
  # return ans
  
  ans = string.replace('-', ' ').replace('_',' ').split()
  
  result = []
  for x in ans:
    result.append(x.capitalize())
  res = ''.join(result)
  return res[0].lowercase()


    
print(camel_case("the_cat_was-kawaii"))
    