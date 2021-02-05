import random
#generate a random number from 1 to 10
secret_number = random.randint(1,10)

# get a number guess from the player
while True:
    guess = int(input("Guess a number between 1 to 10 :\n"))
    
    if guess == secret_number:
        print ('Your got it! my number was {}'.format(secret_number))
        
        break
    else:
        print('Thats not it! ')
       
#compare the guessed secret number
# print hit/miss


