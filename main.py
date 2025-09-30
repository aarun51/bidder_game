from art import logo
print(logo)



bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder = max(bids, key=bids.get)
        print(f"The winner is {find_highest_bidder} with a bid of ${bids[find_highest_bidder]}")
    elif should_continue == "yes":
        print("\n" * 20)
