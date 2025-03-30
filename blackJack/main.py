import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ace_converter(card_list):
    for index in range(len(card_list)):
        if card_list[index] == 11:
            card_list[index] = 1
            break

def user_append(cards_list):
    cards_list.append(random.choice(cards))
    return cards_list

def comp_append(comp_list):
    comp_list.append(random.choice(cards))
    return comp_list

def user_score(cards_list):
    total = 0
    for each_card in cards_list:
        total += each_card
    return total

def comp_score(comp_list):
    total = 0
    for each_card in comp_list:
        total += each_card
    return total

append = {
    "user": user_append,
    "comp": comp_append,
}

game_start = True
while game_start:
    user_starts = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    cards_list = []
    user_total = user_score
    comp_list = []
    comp_total = comp_score

    if user_starts == "y":
        print("\n"*100)
        print(art.logo)
        for i in range(2):
            append["user"](cards_list)
            append["comp"](comp_list)

        print(f"Your cards: {cards_list}, current score: {user_total(cards_list)}")
        print(f"Dealer's first card: {comp_list[0]}")

        if user_total(cards_list) == 21 and comp_total(comp_list) == 21:
            print(f"Both get a Blackjack 😱 It's a draw!!!\n User cards: {cards_list} and Dealer cards: {comp_list}")
            continue

        elif user_total(cards_list) == 21 and comp_total(comp_list) != 21:
            print(f"You get a Blackjack 😱 You Win!!!\n User cards: {cards_list}")
            continue

        elif user_total(cards_list) != 21 and comp_total(comp_list) == 21:
            print(f"Dealer gets a Blackjack 😱 Dealer Wins!!!\n Dealer cards: {comp_list}")
            continue

        game_continue = True
        while game_continue:
            user_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_continue == "y":
                append["user"](cards_list)

                if user_total(cards_list) > 21 and 11 in cards_list:
                    print(f"Your current score is: {user_total(cards_list)} and you got an ace card!! 😓")
                    ace_converter(cards_list)
                    print(f"Ace cards in your deck are converted from 11 to 1 🔄")

                elif user_total(cards_list) > 21:
                    print(f"Busted 😔😔 your Final Hand: {cards_list} is above 21\n Dealer's Final hand: {comp_list}\n Dealer wins, Better luck next time 👍 ")
                    break

                print(f"Your cards = {cards_list}, Your Current Score: {user_total(cards_list)} ")
                print(f"Dealer's first card: {comp_list[0]}")

            elif user_continue == "n":
                # Dealer's turn
                while comp_score(comp_list) < 17:
                    append["comp"](comp_list)


                    if comp_score(comp_list) > 21 and 11 in comp_list:
                        print(f"Dealer's score: {comp_score(comp_list)}. Dealer has an Ace! Converting Ace from 11 to 1... 🤔")
                        ace_converter(comp_list)  # Convert Ace from 11 to 1
                        print(f"Dealer's hand after converting Ace: {comp_list}, Score: {comp_score(comp_list)}")

                if comp_score(comp_list) > 21:
                    print(f"Dealer busted! 😱 Dealer's hand: {comp_list}, Score: {comp_score(comp_list)}.\nYou win! 🎉")

                elif comp_score(comp_list) > user_score(cards_list):
                    print(f"Dealer wins! 😔 Dealer's hand: {comp_list}, Score: {comp_score(comp_list)}\nYour hand: {cards_list}, Score: {user_score(cards_list)}")

                elif comp_score(comp_list) == user_score(cards_list):
                    print(f"It's a draw! 🟰 Your hand: {cards_list}, Score: {user_score(cards_list)}.\nDealer's hand: {comp_list}, Score: {comp_score(comp_list)}")

                else:
                    print(f"You win! 🏆 Your hand: {cards_list}, Score: {user_score(cards_list)}.\nDealer's hand: {comp_list}, Score: {comp_score(comp_list)}")

                game_continue = False

