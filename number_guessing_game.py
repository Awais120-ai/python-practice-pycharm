import random

secret_number = random.randint(1, 20)
attempt = 5

print("🤷‍♀️ welcome to number guessing game! ")
print("guess the number between 1 and 20")
print("you have only five attempts")

while attempt > 0:
    try:
       guess = int(input("enter your Guess: "))
    except ValueError:
       print("please enter a number")
       continue

    if guess == secret_number:
      print("your guess are right")
      break
    elif guess > secret_number:
      print("you are wrong and your number is high ")
    else:
      print("you are wrong and your number is low")
    attempt -= 1
    print("attempt left", attempt)

if attempt == 0:
    print("game over")
