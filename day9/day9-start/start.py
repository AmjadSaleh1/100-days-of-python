from art import logo
print(logo)




bidders = {}


def highest_bidder(bidders):
    max = 0
    max_name = ""
    for key in bidders:
        if bidders[key] > max:
            max = bidders[key]
            max_name = key
    print(f"The winner is {max_name} with a bid of {max}$")


finished_bid = False
while not finished_bid:
    Name = input("Whats youre name?: ")
    bid = int(input("Whats ur bid?: $"))
    bidders[Name] = bid
    Answer = input("Are there any other bidders? type 'yes' or 'no'").lower()
    if Answer == "no":
        finished_bid=True
        highest_bidder(bidders)



