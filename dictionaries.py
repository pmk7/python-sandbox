# user_info = dict(name='Phil',age=33,personality='sparkling')

# index = 1
# for key,val in user_info.items():
#   print(f"line {index} : key is {key}, value is {val}")
#   index += 1
  
  
# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

# total_donations = 0

# for val in donations.values():
#   total_donations += val
#   print(total_donations)
  
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# for key, val in bakery_stock.items():
#   if key == food:
#     print(f"{val} left")
#   else:
#     print("We dont make that")
    
  
# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

# default_val = 0
# initial_game_state = dict.fromkeys(game_properties, default_val)
# print(initial_game_state)

# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}

# stock_list = dict()
# stock_list.update(inventory)
# item = {'cookie': 18}
# stock_list.update(item)
# stock_list.pop('cake')
# print(stock_list)


# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]



# answer = {list1[i] : list2[i] for i in range(len(list1))}
# print(answer)

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# answer = dict(person)
  
# # answer = {i[0]:i[1] for i in person}
# print(answer)  


vowels = 'aeiou'

obj = {i:0 for i in vowels }
print(obj)

  