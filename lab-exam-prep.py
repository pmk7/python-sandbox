# def sum_divisors(num):
#   """print sum of all divisors of argument"""
#   if num < 0:
#     return num
#   else:
#     total = 0
#     sequence = ''
#     for el in range(1,num +1):
#       if num % el == 0:
#         sequence += str(el) + ' + '
#         total += int(el)
#       new_str = sequence[0:-2]
#   print(f"{new_str}= {total}")
  
  

# sum_divisors(42)

# 2.
# sample_str = 'Monty Python'
# encrypted = ''

# for i,char in enumerate(sample_str):
#   encrypted += chr(ord(char) + i) 
#   print(encrypted,i)
  

# 3
# import string

# def format_time(time_string):
#   year, time = time_string.split()
#   year_pieces = year.split('/')
#   time_pieces = time.split(':')
#   if len(time_string) > 19:
#     print('Input is in invalid, try again')
#   elif len(year_pieces) > 3 or int(year_pieces[0]) > 24 or int(year_pieces[1]) > 12 or int(year_pieces[2]) > 2023:
#     print('Years are wrong')
#   elif len(time_pieces) > 3 or int(time_pieces[0]) > 24 or int(time_pieces[1]) > 60 or int(time_pieces[2]) > 60:
#       print('Hour is wrong')
#   return 
      
  
  
# format_time("24/012/2020 18:45:00")

# 4.
# user_input = int(input('Give me a number: '))

# def check_kaprekar(num):
#   total = num * num
#   pieces = [int(x) for x in str(total)]
#   length = len(pieces)
#   middle = length // 2
  
#   piece1_str = ''
#   piece2_str = ''
#   piece3_str = ''
#   piece4_str = ''

  
#   piece1, piece2 = pieces[:middle], pieces[middle:]
#   piece3, piece4 = pieces[:middle + 1], pieces[middle + 1:]

#   for el in piece1:
#    piece1_str += str(el)
#   for el in piece2:
#    piece2_str += str(el)
#   for el in piece3:
#    piece3_str += str(el)
#   for el in piece4:
#    piece4_str += str(el)
   
#   if num == int(piece1_str) + int(piece2_str) or num == int(piece3_str) + int(piece4_str):
#     return True
#   else:
#     return False
    
  
  
# def all_nums(user_input):
#   for el in range(1, user_input):
#     if check_kaprekar(el) == True:
#       print(el)
      

# check_kaprekar(user_input)

# all_nums(user_input)

# 5.
sentence = "I love you for a lifetime not only for a day I love you for who you are not what you do or say"


def reverse_second_word(lst):
  arr = lst.split()
  reversed_lst = []
  for i, el in enumerate(arr):
    if i % 2 == 1:
      reversed_lst.append(el[::-1])
    else:
      reversed_lst.append(el)  
  print(' '.join(reversed_lst))
  
#   for el in reversed_lst:
#     print(el[-1])
    
# def reverse_second_word(lst):
#   arr = lst.split()
#   ans = [x[::-1] for x in arr]
#   print(ans)
    


# reverse_second_word(sentence)

# 6.
def replace_all(string,old,new):
  arr = string.split()
 
  for i,el in enumerate(arr):
    if arr[i] == old[0]:
      arr[i] = new[0]
    if arr[i] == old[1]:
      arr[i] = new[1]  
    if arr[i] == old[2]:
      arr[i] = new[2]  
  print(' '.join(arr))
  
  # old_word = ','.join(old)
  # new_word = ','.join(new)
  

  
# replace_all('This is a wonderful morning',['is','morning'],['was','evening']) 

replace_all("John and Bill went to the shop", ["John","Bill", "shop"],["Mary","Ann","cinema"])