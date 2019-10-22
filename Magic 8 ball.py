import random

while True:
    def magic_8ball():
        return input("What is your question? enter to quit. ")


    Eightball_list = ["It is certain", "Outlook good", "You may rely on it", "Ask again later", "Concentrate and ask again",
                      "Reply hazy, try again", "My reply is no", "My sources say no"]
    if magic_8ball() == "":
        print("exiting...")
    else:
        print(random.choice(Eightball_list))

