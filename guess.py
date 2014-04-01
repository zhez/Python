import random
num = random.randint(1,10)
while True:
    print ('Guess a number between 1 and 10')
    guess = input()
    i = int(guess)
    if i == num :
        print ('Congratulations ! You guessed right !')
        break
    elif i < num :
        print ('Try higher')
    elif i > num :
        print ('Try lower')