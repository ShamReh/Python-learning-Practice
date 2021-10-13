# Guess the secret number 1-10: You have 3 Tries

secret_number = 9
guess_count = 0 
guess_limit = 3

while guess_count < guess_limit:
    guess= int(input('Guess: '))
    guess_count+= 1
    if guess == secret_number:
        print('You win!')
        break
else:
    print('Sorry you lost! Better Luck next time')