# Written: 25-Dec-2019
'''
* Instructions:
*   Create a function that determines whether it is possible to build a palindrome from the characters in a string.
*
*   Examples
*     possible_palindrome("acabbaa") ➞ True
*     # Can make the following palindrome: "aabcbaa"
*     possible_palindrome("aacbdbc") ➞ True
*     # Can make the following palindrome: "abcdcba"
*     possible_palindrome("aacbdb") ➞ False
*     possible_palindrome("abacbb") ➞ False
*
*   Notes
*   N/A
*
* Resources: https://en.wikipedia.org/wiki/Palindrome
'''

# =======================================================================================

def possible_palindrome(txt):
    odd_letter = 0              # Storing sum of odd letter
    for letter in set(txt):     # Convert to set, prevent duplicate letter
        if txt.count(letter) % 2 == 0:
            continue
        odd_letter += 1
    if odd_letter > 1:
        return False
    return True
    # Concept: The sum of odd letter must be <= 1,
    # while sum of all other letter(s) must be even

    # return sum(txt.count(letter)%2 for letter in set(txt)) <= 1


print(possible_palindrome("acabbaa"))   # True
print(possible_palindrome("aacbdbc"))   # True
print(possible_palindrome("aacbdb"))    # False
print(possible_palindrome("abacbb"))    # False