# Good Price software

import random


def main():
    estimate_price = 0
    try_number = 4
    round_number = 3
    round_win = 0

    while round_number > 0 and round_win < 2:
        # Set a random number
        good_price = random.randint(1, 3)
        print(good_price)

        while estimate_price != good_price and try_number > 0:
            estimate_price = win_price()

            if estimate_price == good_price:
                print("Got it")

            elif estimate_price < good_price:
                print("It's more")
            else:
                print("It's less")

            try_number = try_number - 1
            print(try_number, "try left")

        if try_number > 0:
            print("Round Win")
            round_win = round_win + 1
            estimate_price = 0
        else:
            print("Round Loose")
            estimate_price = 0

        round_number = round_number - 1
        try_number = 4

    if round_win >= 2:
        print("Win game")
    else:
        print("Loose game")


def win_price():
    # Ask to user to make a try
    while True:
        try:
            estimate_price = int(input("Tell a price : "))
            return estimate_price
        except ValueError:
            print("You have to enter an estimate price")


if __name__ == "__main__":
    main()
