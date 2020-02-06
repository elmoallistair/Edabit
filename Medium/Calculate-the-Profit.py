# Written: 07-Dec-2019
'''
* Instructions:
*   You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product.
*   You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory.
*   Return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold.
*
*   Examples
*     profit({
*       "cost_price": 32.67,
*       "sell_price": 45.00,
*       "inventory": 1200
*     }) ➞ 14796
*
*     profit({
*       "cost_price": 225.89,
*       "sell_price": 550.00,
*       "inventory": 100
*     }) ➞ 32411
*
*     profit({
*       "cost_price": 2.77,
*       "sell_price": 7.95,
*       "inventory": 8500
*     }) ➞ 44030
*
*   Notes
*     Profit = Total Sales - Total Cost
*
* Resources:
*   - www.tutorialspoint.com/python/python_dictionary.htm
*   - https://www.programiz.com/python-programming/methods/built-in/round
*   - https://www.programiz.com/python-programming/methods/built-in/dict
'''

# =======================================================================================

def calculate(info):
    price = (info["sell_price"] - info["cost_price"]) * info["inventory"]
    return round(price)

product1 = {
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}
product2 = {
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}
product3 = {
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}

print(calculate(product1))  # Output: 14796
print(calculate(product2))  # Output: 32411
print(calculate(product3))  # Output: 44030


