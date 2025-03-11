print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
cross_road = str(input("You are at a cross road. where do you want to go ? \n Type 'left' or 'right'? \n"))


if cross_road == "left" :
    left_action = str(input("You have come to a lake, There is an island in the middle of the lake. \n You can type 'swim' to swim across the lake or type 'wait' to wait for a boat \n"))
    if left_action == "wait":
        island_action = str(input("You arrived at the island unharmed, There is a house with 3 doors. \n one 'yellow', one 'red' and one 'blue'. Which one do you choose ? \n"))
        if island_action == "blue":
            print("Congratulations you found the treasure!!!!")
        elif island_action == "red":
            print("You got transported to the start of the game! Start over")
        else:
            print("BOOM!!!! There was an explosion and you died! Game Over!!")
    else:
        print("You got attacked by an angry trout. GAME OVER!!")
else:
    print("You fell into a hole. Better luck next time")