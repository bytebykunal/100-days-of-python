gavel = r''' 
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\ '''

print(gavel)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bidders = {}
again = "yes"
while again != "no":
    name = input("What is Your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    again = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if again == "yes":
        print("\n" * 20)
    elif again == "no":
        find_highest_bidder(bidders)
