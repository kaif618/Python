from art import logo, vs
from random import choice
from game_data import data
print(logo)

score = 0
random_celeb_compare=choice(data)
game_continues = True
while game_continues:

    print(f"Compare A: {random_celeb_compare['name']}, a {random_celeb_compare['description']}, from {random_celeb_compare['country']}")
    print(vs)

    random_celeb_against = choice(data)

    while random_celeb_compare == random_celeb_against:
        random_celeb_against = choice(data)

    print(f"Against B: {random_celeb_against['name']}, a {random_celeb_against['description']}, from {random_celeb_against['country']}")
    user_answer = input("Who has more followers, Type 'A' or 'B': ").lower()

    celeb_1_followers = random_celeb_compare["follower_count"]
    celeb_2_followers = random_celeb_against["follower_count"]

    if (user_answer == "a" and celeb_1_followers > celeb_2_followers) or (user_answer == "b" and celeb_2_followers > celeb_1_followers):
        score += 1
        print(f"You are right!!! Current score: {score}.")
        random_celeb_compare = random_celeb_against
    else:
        print("\n" * 100)
        print(logo)
        print(f"Sorry that's wrong!!! Your Final Score: {score}")
        game_continues = False
