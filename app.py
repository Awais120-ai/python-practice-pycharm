person_name = 'Awais'
fav_color = 'blue'
print("mosh likes " + fav_color)

for item in "python":
    print(item)

names = ['ali', 'ahmad', 'zain', 'awais', 'basit']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names)

# list methods ...............

numbers = [5, 6, 7, 3, 9, 1]
# numbers.insert(0, 8)
# numbers.clear()
# numbers.append(9)
numbers.pop()
print(numbers)

numbers = [5, 6, 7, 8, 9, 0]
print(numbers.count(5))
# print(numbers.sort())
print(numbers)

# write a program to remove a duplicates in a list

numbers = [5, 6, 7, 7, 8, 8, 9]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
    print(uniques)

# unpacking topic ........ is ma ap kleft side or right side k variables equal hony chaiyee (it means value ko tor kar variables ma dalna unpacking kehlata ha)

numbers = [5, 4, 3, 2, 1]
a, b, c, d, e = numbers
print(a)
print(b)

# dictionaries topic ...............

customer = {"name": "Awais", "age": 23, "is_verified": True, "city": "Rawalpindi"}
# print(customer["name"])
# print(customer)
del customer["is_verified"]
print(customer)


# .....  functions ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# def keyword se function banate hain
# Function ko call karna zaroori hota hai
# Parameters input hote hain
# Return output deta hai


def greet():
    print("Hello! Welcome to Python")


greet()


# function with parameters

def greet(name):
    print("Hello", name)


greet("Awais")


# function with return value........

def add(x, y):
    return x + y


result = add(5, 3)
print(result)


def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}")

    # It is called an f - string(formatted string literal)
    # .It is used to insert (variables and expressions)
    # directly inside a string using
    # curly braces {}. 👍


print("start")
greet_user("Awais", "Ahmad")
print("finish")


# ........... return statement ........

def square(numb):
    return numb * numb


result = square(5)
print(result)

# ....................exception handling ...........

try:
    num = 10
    print(num / 0)

except ZeroDivisionError:
    print("You cannot divide by zero.")

    # ........ multiple exceptions ......

    try:
        num = int(input("Enter a number: "))
        print(10 / num)

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except ValueError:
        print("Please enter a valid number.")

        # ..........................................//
    try:
        num = int(input("Enter a number: "))

        print(num / 3)

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except ValueError:
        print("Please enter a valid number.")

        # .........................................

        try:
            num = int(input("Enter a number: "))

            if num % 2 != 0:
                print("Number is odd, but still dividing...")

            print(num / 3)

        except ValueError:
            print("Invalid input.")

# ........................................................

try:
    age = int(input("Age: "))
    income = 500000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("income can not be divided by zero.")
except ValueError:
    print("invalid value")


# ...............classessss..............................
# classes is a blueprint jis se hum object banate hain
# 👉 Simple example:
# Socho ek Car factory hai.
# Class = Car ka design (blueprint)
# Object = actual car (Honda, Toyota)

class Point:
    @staticmethod
    def move():
        print("you moved towards point")

    @staticmethod
    def draw():
        print("you drawn towards point")


point1 = Point()
point1.x = 10
point1.y = 20

print(point1.x)
point1.draw()


class Student:
    @staticmethod
    def eng():
        print("he got 50 maks")

    @staticmethod
    def fren():
        print("he got 20 maks")

    @staticmethod
    def mars():
        print("he got 0 maks")

    @staticmethod
    def result():
        print("he got 100 maks and he is a good student in whole class")


teacher = Student()
teacher.a = 'Muhammad'
teacher.b = 'Awais'
print(teacher.a, teacher.b)
teacher.result()


# .................................................
# .........................constructor....................
# .................................................

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


s1 = Student("Awais", 20)
s1.show()
