import random


player = input("player...rock...paper...scissors ")
rand_int = random.randint(0,2)
if rand_int == 0:
  comp_player = 'rock'
elif rand_int == 1:
  comp_player = 'paper'
else: comp_player = 'scissors'    

if player == comp_player:
  print('Tie!')
 