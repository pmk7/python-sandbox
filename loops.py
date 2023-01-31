# x = 0
# for num in range(10, 20):
#   if num % 2 != 0:
#    x += num
#    print(x)

# clean_room_num = int(input('How many times do i have to tell you to clean up your room? '))

# for times in range(clean_room_num):
#   print('CLEAN UP YOUR ROOM!')

# for times in range(1,21):
#   if times % 2 == 1:
#     state = 'odd'
#   elif times % 2 == 0:
#     state = 'even'
#   if times == 4 or times == 13:
#     state = 'unlucky'
#   print(f'{times} is {state}')
 
# for x in range(3):
#     for num in range(1,11):
#         print('\U0001f600' * num)


# times = 1
# while times < 11:
#   print(' ' + '\U0001f600' * times)
#   times += 2

# sentence = 'Hey, stop repeating what I say! '
# print(sentence * 3)

# headcount = 11
# for num in range(1,headcount):
#     space = (" " * (headcount - num))
#     print(space + "\U0001f600" * num)

# msg = input('Say something: ')

# stop = 'stop copying me!'
# times_repeat = 1
# while msg != stop:
#   print(msg)
#   msg = input()
import random

ran = random.randint(1, 10)
user = None
while user != ran:
     user = int(input('Guess a number between 1 and 10: '))
     if user < ran:
        print('TOO LOW!')  
     elif user > ran:
        print('TOO HIGH!')
     else:
        print('YOU GUESSED IT!')





