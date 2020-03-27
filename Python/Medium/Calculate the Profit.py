# Written: 07-Dec-2019
# https://edabit.com/challenge/YfoKQWNeYETb9PYpw

def profit(info):
    price = (info["sell_price"] - info["cost_price"]) * info["inventory"]
    return round(price)