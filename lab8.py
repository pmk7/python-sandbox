# LISTS

# 1.
sample_lst = [1,2,3,7,4,5,6]

# def total(lst):
#   el_total = 0
#   for i in lst:
#     el_total += i
#   return el_total
    
# print(total(sample_lst))

# 2

# def largest(lst):
#   biggest = lst[0]
#   for i in lst:
#     if i > biggest:
#       biggest = i
#   return biggest 


# print(largest(sample_lst))     


# 3.
words =  ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']


# def calc_o_words(lst):
#   counter = 0
#   for el in words:
#     if el[0] == 'o':
#       counter += 1
#   return counter
    
# print(calc_o_words(words)  )      

# 4.
# def check_if_char_in_list(words, letter):
#   counter = 0
#   for el in words:
#     if el[0] == letter:
#       counter += 1
#   return counter


# print(check_if_char_in_list(words, 'a'))
  
# 5.
# def even_num_lst(lst):
#   evens = []
#   for el in lst:
#     if el % 2 == 0:
#       evens.append(el)
#     return evens

# print(even_num_lst(sample_lst) )

# 6
# nums = list(range(0,101))
# print(nums[5])

# 7
num_list = [1,1,1,1,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6]

# def remove(lst):
#   unique = []
#   for i in lst:
#     if i not in unique:
#       unique.append(i)
#   return unique


# print(remove(num_list))

# 8

nums1 = [1,2,3,4,5,6]
nums2 = [10,9,8,7,6]

# def compare_list(nums1, nums2):
#   for el in nums1:
#     if el in nums2:
#       return True
    
#   return False
      
  
# def compare_list(nums1, nums2):
#   unique = []
#   for el in nums1:
#     for i in nums2:
#       if i != el:
#         print(el, i)
#         # unique.append(i)
#     # return unique    
      
  
  
# print(compare_list(nums1, nums2))

# 10.
sample = [11,33,50]

def num(lst):
  total = ''
  for el in lst:
    total += str(el)
  print(int(total))


num(sample)

# 11.
listA = [10,20,30,40,50]

def add_neighbors(lst):
  count1 = 0
  count2 = 1
  new_list = []
  for i in listA:
    if (len(listA) == 1):
      new_list = listA
    elif i == 0:
    
    else:
    new_list.append(listA[i - 1] + listA[i] + listA[i + 1])
  
  
add_neighbors(listA)