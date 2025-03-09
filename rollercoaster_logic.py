height = int(input("Enter your height in cm? \n"))
ticket = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? \n"))
    if age <=12:
        print("child tickets are $5.")
        ticket = 5
    elif age<=18:
        print("Youth tickets are $7.")
        ticket = 7
    else:
        print("Adult  tickets are $12.")
        ticket = 12
    img = input("Do you want a photo take for rollercoaster ? Type Y for yes and N for no ")
    if img == "Y":
        ticket += 3
        print("The price is $3 \n")
    print(f"Your final bill will be: ${ticket}")
else:
    print("You can't ride the rollercoaster")
