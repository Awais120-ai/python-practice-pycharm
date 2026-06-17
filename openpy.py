# import openpyxl as xl
# xl.load_workbook('transactions.xlsx')
# sheet = wb['sheet1']
# cell = sheet['A1']
# cell = sheet.cell(row=1, column=1)
#
# for row in range(2, sheet.max_row + 1):
#     cell = sheet.cell(row, 3)
#     print(cell.value)
#     print(row)
#

names = ["john", "mary"]
found = False
for name in names:
    if name.startswith("j"):
        print("found")
        found = True
        break
else:
    print("not found")


    # ..............................................................
# ......................... while loop ................................
# ............................... gane  ..................................


answer = 5

while True:
    guess = int(input("Guess: "))

    if guess == answer:
        print("You guessed it right!")
        break
    else:
        print("Try again!")




# ....................... fizzbuzz...........................


def fizz_buzz(input):
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    return input
print(fizz_buzz(5))