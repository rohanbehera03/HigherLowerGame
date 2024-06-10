import random
import os
import game_art
import game_database

print(game_art.game_logo)
score = 0

def display_accountinfo(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, account1_followers, account2_followers):
    if account1_followers < account2_followers:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 2:
            return False
        else:
            return True

account2 = random.choice(game_database.data)

continue_flg = True  
while continue_flg:
    account_1 = account2
    account_2 = random.choice(game_database.data)
    while account_1 == account2:
         account_2 = random.choice(game_database.data)
 
    print(f"Compare 1: {display_accountinfo(account_1)}")
    print(game_art.vs)
    print(f"Compare 2: {display_accountinfo(account_2)}")
    guess = int(input("Who has more followers? Type '1' or '2': "))
    account1_followers = account_1['follower_count']
    account2_followers = account_2['follower_count']
    is_correct = check_answer(guess, account1_followers, account2_followers)

    os.system('clear')
    print(game_art.game_logo)
    
    if is_correct:
        score += 1
        print(f"You are right. Your score is {score}")
    else:
        print(f"You are wrong...Your final score is {score}")
        continue_flg = False

