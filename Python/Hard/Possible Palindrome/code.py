# Written: 25-Dec-2019
# https://edabit.com/challenge/pTtzfmR2z7jqYXJDf

def possible_palindrome(txt):
    odd_letter = 0              # Storing sum of odd letter
    for letter in set(txt):     # Convert to set, prevent duplicate letter
        if txt.count(letter) % 2 == 0:
            continue
        odd_letter += 1
    if odd_letter > 1:
        return False
    return True

    # return sum(txt.count(letter)%2 for letter in set(txt)) <= 1
