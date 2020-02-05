# Written: 09-Dec-2019
'''
* Instructions:
*   Make a function that encrypts a given input with these steps:
*   Input: "apple"
*   Step 1: Reverse the input: "elppa"
*   Step 2: Replace all vowels using the following chart:
*     a => 0
*     e => 1
*     o => 2
*     u => 3
*
*     # "1lpp0"
*
*   Step 3: Add "aca" to the end of the word: "1lpp0aca"
*   Output: "1lpp0aca"
*   Examples
*     encrypt("banana") ->➞ "0n0n0baca"
*     encrypt("karaca") ->➞ "0c0r0kaca"
*     encrypt("burak") ->➞ "k0r3baca"
*     encrypt("alpaca") ->➞ "0c0pl0aca"
*
*   Notes
*   All inputs are strings, no uppercases and all output must be strings.
*
* Resources:
*   - https://www.journaldev.com/23697/python-string-translate#maketrans-with-one-argument
*   - https://www.programiz.com/python-programming/methods/string/replace
*   - https://www.journaldev.com/23647/python-reverse-string
'''

# =======================================================================================

def encrypt(word):
    word = (word[::-1]).lower()
    trans = word.replace('a', '0').replace('e', '1').replace('o','2').replace('u','3')
    return trans+'aca'

    # Shorter code:
    # return word[::-1].translate(str.maketrans('aeou', '0123')) + 'aca'

print(encrypt("banana"))    # Output: "0n0n0baca"
print(encrypt("karaca"))    # Output: "0c0r0kaca"
print(encrypt("burak"))     # Output: "k0r3baca"
print(encrypt("alpaca"))    # Output: "0c0pl0aca"