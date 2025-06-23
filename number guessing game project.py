
import random

print('======')
print('NUMBER GUESSING GAME')
print('======')
print('THE NUMBER RANGES BETWEEN 1 TO 100')
#giving a random number
secret_num =random.randint(1,100)
#limit the no. of tries
attempts=0
m_attempts=10
#starting the game
while attempts<m_attempts:
    guess=int(input('guess the number:'))
    attempts += 1
    if guess<secret_num:
        print('nahhh try again')
    elif guess>secret_num:
        print('Omg its too high try again')
    else:
        print('hurray!!!you got it!')


    
