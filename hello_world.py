# name = input( "What is your name?")
# print(" Hi " + name)


fav_color = input("What is your favourite color?")
print(" manna likes " + fav_color)

Course = "What is your favourite course?"
print(Course.upper())
print(Course.lower())

Course = "What is your favourite course?"
print(Course.replace('a', 'l'))
print(Course.find('a'))
print(Course.find('e'))

is_hot = False
if is_hot:
    print("it is hot day")
    print("drink plenty of water")
    print("enjoy your day")
else:
    print("not hot day")
    print("enjoy your day")

    secret_number = 9
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        print("Attempt:", guess_count + 1)
        guess = int(input("guess: "))
        guess_count += 1
        if guess == secret_number:
            print('you won it')
            break
    else:
        print('sorry you failed')

command = ""
while command != "quit":
    command = input("> ")
    if command == "start":
        print("car started.....")
    elif command == "stop":
        print("car stopped.....")
    elif command == "help":
        print("""
            start - to start the car
            stop  - to stop the car
            quit - to quit the car
            """)
    else:
        print('sorry i did not understand that !')


# command = ""
# car_started = False   # memory of car status
#
# while command != "quit":
#     command = input("> ").lower()
#
#     if command == "start":
#         if car_started:
#             print("⚠️ Car is already started!")
#         else:
#             car_started = True
#             print("🚗 Car started...")
#
#     elif command == "stop":
#         if not car_started:
#             print("⚠️ Car is already stopped!")
#         else:
#             car_started = False
#             print("🛑 Car stopped...")
#
#     elif command == "help":
#         print("""
# Available commands:
# start - start the car
# stop  - stop the car
# quit  - exit the program
# help  - show commands
# """)
#
#     elif command == "quit":
#         print("👋 Goodbye!")
#
#     else:
#         print("❌ Sorry, I didn't understand that!")
