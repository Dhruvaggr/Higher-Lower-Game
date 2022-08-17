#Higher or lower game

# Data and Logo of this game can be view by the link given in Readme file
from replit import clear
from art import logo

print(logo)
from game_data import data
#print(data)
import random


def compare(current_score):

    C = random.randint(0, len(data) - 1)
    D = random.randint(0, len(data) - 1)

    print(
        f"Compare A: {data[C]['name']},a {data[C]['description']}, from {data[C]['country']}"
    )

    from art import vs
    print(vs)

    print(
        f"Against B: {data[D]['name']},a {data[D]['description']}, from {data[D]['country']}"
    )

    A = data[C]['follower_count']
    B = data[D]['follower_count']
    should_continue = True
    while should_continue == True:
        Question_to_user = input("Who has more Followers? Type 'A'or'B': ")

        if (Question_to_user == 'A' and A > B) or (Question_to_user == 'B'
                                                   and B > A):
            clear()
            current_score = current_score + 1
            print(f"You are right! current score is:{current_score}")

        else:
            clear()
            print(f"You are wrong! your final score is:{current_score}")
            break
        should_continue = False
        
        compare(current_score)


current_score = 0

compare(current_score)
