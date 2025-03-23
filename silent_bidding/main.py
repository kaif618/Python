from art import logo
print(logo)

def finding_highest_bid(bids):
    highest_bid = 0
    name_value = ""
    for keys in bid_data:
        if bid_data[keys] > highest_bid:
            highest_bid = bid_data[keys]
            name_value = keys
    print(f'{name_value} has the highest bid value ${highest_bid}')

bid_data = {}
bidding = True

while bidding:
    name = str(input("What is your name ? "))
    price = int(input("What's your bid ?: $"))
    bid_data[name] = price

    user_add = input("Is there any other user, that wants to bid ? Type 'Y' for yes and 'N' for no: ").lower()
    if user_add == "n":
       bidding = False
       finding_highest_bid(bid_data)
    else:
        print("\n"*100)



