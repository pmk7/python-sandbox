# def square(num): return num * num

# # TYPICALLY NOT STORED IN A VARIABLE
# square2 = lambda num: num * num

# cube = lambda num: num ** 3

# print(cube(3))

# nums = [2,3,4,5]

# doubles = map(lambda x: x**2, nums)
# print(list(doubles))
# nums = [2,3,4,5]

# decrement_list = list(map(lambda num: num - 1, nums))

# print(decrement_list)

# LAMBDA FILTER

# users = [
#   {"username":"sam","tweets":["Hi, there", "What a day!"] },
#   {"username":"bill","tweets":[]},
#   {"username":"tom","tweets":[]},
#   {"username":"phil","tweets":[]}
#   ]

# inactive_users = list(filter(lambda i: not i["tweets"], users))

# print(inactive_users[0])

# print([user for user in users if not user["tweets"]])



# LIST COMPREHENSIONS- CLEANER SOLUTION

# names = ["Phil", "Ira", "Cornelius"]

# print([f"Your instructor is {name}" for name in names if len(name)> 5])

# GENERATOR EXPRESSION
# def is_all_strings(lst):
#     return all(type(l) == str for l in lst)

# # LIST COMPREHENSION
# is_all_strings = any([type(i) == str for i in ['a','hi', 5]])

# print(is_all_strings)


# users = [
#   {"username":"sam","tweets":["Hi, there", "What a day!"] },
#   {"username":"bill","tweets":[]},
#   {"username":"tom","tweets":[]},
#   {"username":"phil","tweets":[]}
#   ]

# print(sorted(users,key=lambda user: len(user['tweets']), reverse=True))

