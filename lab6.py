# STRING METHODS

# 1
# s = "CAT"
# print(s.upper().lower())

# Yes, second string method overwrites first

# 2
# user = input("I'll convert to lowercase ")
# print(user.lower())

# 3
# some_string = "Hello world!"
# print(some_string.count("o"))
# count method returns number of times character appears in string 

# 4
# word = "Bye         "
# print(len(word))
# print(word.strip())
# stripped_word = word.strip()
# print(len(stripped_word))
# some_string = "Hi!......"
# print(some_string.strip(".!"))
# Strip method removes all characters entered as an argument, or whitespace if no argument passed

# 5
# a
# print("#" * 30, "\n", "#" * 20 )

# b

# 6
# ab_string = 'abababababababab'
# new_string = ''

# for i in ab_string:
#   if i != 'b':
#     new_string += i
    
# print(new_string)

# 7
name = "Name"
melt = "Melting Point (deg C)" 
boil = "Boiling Point (deg C)" 


gas1 = 'Methane'
melting_p_gas1 = '-162'
boiling_p_gas1 = '-182'

gas2 = 'Ethane'
melting_p_gas2 = '-89'
boiling_p_gas2 = '-172'

gas3 = 'Propane'
melting_p_gas3= '-42'
boiling_p_gas3 = '-188'

gas4 = 'Butane'
melting_p_gas4 = '-162'
boiling_p_gas4 = '-182'


# print("Melting and Boiling Points of Alkanes\n{:<5s} {:>28s}{:>30s}".format(name, melt, boil))
# print("{:<5s}{:>10s}{:>30s}".format(gas1, melting_p_gas1, boiling_p_gas1))
# print("{:<5s}{:>10s}{:>31s}".format(gas2, melting_p_gas2, boiling_p_gas2))
# print("{:<5s}{:>9}{:>31s}".format(gas3, melting_p_gas3, boiling_p_gas3))
# print("{:<5s}{:>11s}{:>30s}".format(gas4, melting_p_gas4, boiling_p_gas4))

# 8
# string = "Hello World"
# import random
# ran_num1 = random.randint(1,10)
# ran_num2 = random.randint(1,10)
# print(string.replace(string[ran_num1],string[ran_num2]))



# 9
user_word = input("I'll give you the Latin word back: ")


if user_word[0] in 'aieou':
  print(f"{user_word}yay")
elif user_word[0] not in 'aieou':
    transform = user_word[1:] + user_word[:len(user_word) - 1]
    print(f"{transform}ay")


# index = 0
# transform = ''
# while user_word[index] not in 'aieou' and index < 10:
#   transform += user_word[index]
#   print(transform)
#   index + 1