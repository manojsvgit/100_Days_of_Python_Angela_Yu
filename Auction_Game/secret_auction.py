import pyfiglet
from logo import logo_hammer
print(logo_hammer)

logo_text="Secret Auction"
print(pyfiglet.figlet_format(logo_text))
auction = {}

def bidding():
    name = input("Enter your name: ")
    bid_price = int(input("Enter your BID amount: "))
    auction[name] = bid_price

bidding()
should_continue = True
while should_continue:
    bidder = input("\nIs there any other user to BID? (yes/no)\n")

    if bidder.lower() == "no":
        should_continue = False
        highest_bidder = max(auction, key=auction.get)
        max_bid = auction[highest_bidder]
        print(f"The Highest Bidder is {highest_bidder} with a bid amount of {max_bid}")
    else:
        #print("\n" * 100)
        bidding()

print(auction)
