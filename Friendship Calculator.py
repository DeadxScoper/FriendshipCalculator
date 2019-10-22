import random

first = input("First person:")
second = input("Second person:")

for x in range(1):
    number = (random.randint(0, 101))
    print(number)
    if number < 50:
        print("{} and {} dont like each other ".format(number,first, second))
    elif 50 >= number <= 75:
        print("There is chance between you")
    else:
        print("There is a very good chance love will be sustained")
