import random

secret_number = random.randint(1,100)

guess = 0

print ("---------------------")
print ("welcome to number guessing game.")
print ("guess a number between 1 to 100.")
print ("---------------------")

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print ("wrong guess.")
        continue

    if guess < secret_number:
        print ("think of a greater number.")

    elif guess > secret_number:
        print ("think of a smaller number.")


print (f"CONGRATULATIONS!!! You guessed the number = {secret_number} correctly.")