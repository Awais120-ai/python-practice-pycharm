# /................/....User se name lo aur print karo:.....


n = input("enter name: ")
print("Hello", n + ", welcome to python!")

# .....................................
# .........User se number lo aur check karo:
#
# even hai ya odd
# .....................................


number = int(input("enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")


    # .....................Simple Calculator......................

    number1 = int(input("enter a number: "))
    operator = input("enter operator: (+,-,/,*): ")
    number2 = int(input("enter a number: "))

    if operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "/":
        if number2 != 0:
            print("Result: ", number1 / number2)
        else:
            print("it can not be divided by 2")
    elif operator == "*":
        print(number1 * number2)

    else:
        print("invalid operator")


# ..................loop practise..............................


for number in range(1, 51):
    if number % 2 == 0:
        print(number)

for number in range(1, 51):
    if number % 2 != 0:
        print(number)



# ..............Mini Game (Guess Number)........................

number = 7

while True:
    guess = int(input("Guess: "))

    if guess == number:
        print("You guessed it right!")
        break
    else:
        print("Try again!")
