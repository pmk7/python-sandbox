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


# def camel_case(string):  
#   ans = string.replace('-', ' ').replace('_',' ').split()
  
#   result = []
#   for i,x in enumerate(ans):
#     if i == 0:
#       result.append(x)
#     else:
#       result.append(x.capitalize())
  
#   res = ''.join(result)
#   return res



    
# print(camel_case("the_cat_was-kawaii"))

# def score(dice):
#     ones = ''
#     twos = ''
#     threes = ''
#     fours = ''
#     fives = ''
#     sixes = ''
    
#     score = 0
    
#     for num in dice:
#       if num == 1:
#         ones += str(1)
#       elif num == 2:
#            twos += str(2)
#       elif num == 3:
#         threes += str(3)
#       elif num == 4:
#         fours += str(4)
#       elif num == 5:
#         fives += str(5)
#       else:
#         sixes += str(6)
        
#     if len(ones) == 3:
#       score += 1000
#     elif len(ones) == 4:
#       score += 1100
#     return print(score)   
     
     
  
    
    
# score([1, 1, 1, 1, 2])   
 
# def persistence(n): 
#   """"return number of times it takes to reduce n to single digit"""
#   counter = 0
#   res = n
#   if res < 10:
#    return counter
#   else:
#     counter += 1
#     ans = str(res)
#     # Only works on two digit numbers
#     res = int(ans[0]) * int(ans[1]) 
#     print(res)
#     return persistence(res) 
    
#   #  return print(counter)
      
    
# persistence(39)
# # print(persistence(729))
# print(persistence(126))


# def sum_of_intervals(intervals):
#   ans = 0
#   for el in intervals:
#     if el == temp
#     print(el)
#     temp = el[1]
#     ans += temp - el[0]

#   # return ans
  
# print(10 - -100000000)  
  
# print(sum_of_intervals([
#    [1, 4],
#    [7, 10],
#    [3, 5]
# ])  )
# print(sum_of_intervals([(1, 5],[6, 10)] ))


# print(sum_of_intervals([
#    [1, 2],
#    [6, 10],
#    [11, 15]
# ] ))

# print(sum_of_intervals( [
#    [1, 5],
#    [10, 20],
#    [1, 6],
#    [16, 19],
#    [5, 11]
# ] ))
  
  
def first_non_repeating_letter(string):
  if len(string) == 0:
    return
  
  ans = []
  for letter in string:
    print(string.lower())
    if string.count(letter) == 1:
      ans.append(letter)
    print(ans)  
  
  return ans[0]  
    
# print(first_non_repeating_letter('sTreSS')  )


def format_duration(seconds):
  minutes,seconds = divmod(seconds,60)
  hours,minutes = divmod(minutes,60)
  days, hours = divmod(hours,24)
  years,days = divmod(days,365)
  
  
    

  

format_duration(62)

