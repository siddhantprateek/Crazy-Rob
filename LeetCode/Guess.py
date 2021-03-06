import random

secret_number = random.randint(1, 10)
print("Think a number b/w 1 to 10")

for guessTaken in range(1, 7):
    guess = int(input('Take a Guess:'))

    if guess < secret_number:
        print("Your number is too low.")
    elif guess >secret_number:
        print("Your number is too high.")
    else:
        break

if guess == secret_number:
    print('Great job!  you guessed it right in ' + str(guessTaken) + ' attempt')
else:
    print("the secret number was" + str(secret_number))
