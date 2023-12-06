import random

attemps_list = []

attemps = 0

def show_score():
    if not attemps_list:
        print("there\'s no currently high score, you should play at least one game")
    else:
        print(f"the current high score is {min(attemps)} attemps")


print("welcome to the guessing game!")
wanna_play = input("do you want to play? (yes/no): ").lower()
if wanna_play == "yes":
    print("cool, let\'s start!")
else:
    show_score()

rand_num = random.randint(1, 10)

while wanna_play == "yes":
    guess = int(input("guess a number between 1 and 10: "))
    try:
        if guess not in range(1, 11):
            raise ValueError("please enter a number in the giver range")
        
        attemps += 1

        if guess == rand_num:
            attemps_list.append(attemps)
            print("woohoo! you did it")
            print(f"it took you {attemps} attemps")
            
            wanna_play = input("would you like to play again? (yes/no): ").lower()
            if wanna_play == "yes":
                attemps = 0
                rand_num = random.randint(1, 10)
                print(f"the high score is {min(attemps_list)}")
            else:
                print("have a nice day")

        elif guess > rand_num:
            print("answer\'s lower")

        else:
            print("answer\'s higher")

    except ValueError as error:
        print(error)
