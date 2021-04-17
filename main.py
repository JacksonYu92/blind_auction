from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

bidders_prices = {}

def auction (bidder_name, bidder_bid):
    bidders_prices[bidder_name] = bidder_bid





auction_continued = True
while auction_continued:

    name = input("What is your name?: ")
    bid = input("Waht is your bid?: $")
    auction(name, bid)
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

    if other_bidders == "yes":
        clear()

    elif other_bidders == 'no':
        auction_continued = False
        highest_bid = 0
        for name in bidders_prices:   
            if int(bidders_prices[name]) > highest_bid:
                highest_bid = int(bidders_prices[name])
                highest_bidder = name
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}!")