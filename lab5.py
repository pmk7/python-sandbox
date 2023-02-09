# STRINGS

# 1.
# my_str = 'Hello World'

# for i in my_str:
#   print(i)

# 2  
# print(len(my_str)) 

# 3
# film = 'Monty Python'

# # a
# print(film[0]) 
# # b
# print(film[-1]) 
# # c
# print(len(film[-1])) 
# # d
# print(film[:5]) 

# 4
# odd_str = 'phone'

# # a
# str_length = len(odd_str)
# ans = odd_str[str_length // 2]
# print(ans)

# index = str_length // 2
# print(index)
# # b
# # print(odd_str[0:index])

# # c
# print(odd_str[index + 1:])


# 5
# s1 = "concord" 
# s2 = "souix city"
# s3 ="HONOLULU"
# s4 = "TopHat"

# a capitalize transforms string[0] to uppercase
# b swapcase transforms all characters in string to uppercase or lower case depending on the initial
# c upper transforms all characters in string to uppercase
# d lower transforms string[0] of each separate word to upper
# print(s2.title())

# 6

str_word = 'Hello World'

# 7
# reversed_str = ''
# for item in str_word:
#   reversed_str = item + reversed_str
# print(reversed_str)


# print(ord('a'))
# print(ord('b'))


# 8

# sample_str = 'abc'
# output_str = ''

# for item in sample_str:
#   unicode_val = ord(item) + 1
#   output_str += chr(unicode_val)
  
# print(output_str)

# 9
sample_int = int(input('Give me a number: '))
binary_str = ''


if (sample_int != 0):
  while (sample_int >= 1):
    if(sample_int % 2== 0):
      binary_str = binary_str + "0"
      sample_int = sample_int / 2
    else:
      binary_str = binary_str + "1"
      sample_int = (sample_int -1) /2

print(binary_str)      


# reversed_str = ''
# for item in binary_str:
#   reversed_str = item + reversed_str
  
# print(reversed_str)

# binary_to_int = 0
# print(type(binary_str))
# for i in binary_str:
#   binary_to_int += i ** 2
# print(binary_to_int)

binary_to_int = 0
index = 0

for item in binary_str:
  binary_to_int += (2 ** index * int(item))
  print(binary_to_int)
  index += 1

print(binary_to_int)


    
    