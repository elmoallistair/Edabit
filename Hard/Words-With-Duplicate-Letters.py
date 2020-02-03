# Written: 12-Dec-2019
'''
* Instructions:
*   Given a common phrase, return False if any individual word in the phrase contains duplicate letters.
*   Return True otherwise.
*
*   Examples
*     no_duplicate_letters("Fortune favours the bold.") ->➞ True
*     no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ->➞ True
*     no_duplicate_letters("Look before you leap.") ->➞ False
*     # Duplicate letters in "Look" and "before".
*     no_duplicate_letters("An apple a day keeps the doctor away.") ->➞ False
*     # Duplicate letters in "apple", "keeps", "doctor", and "away".
*
*   Notes
*   Letter matches are case-insensitive.
*
* Resource:
*   - https://www.programiz.com/python-programming/methods/string
*   - https://docs.python.org/2/library/collections.html#counter-objects
*   - https://www.w3schools.com/python/ref_string_split.asp
'''

# =======================================================================================

def no_duplicate_letters(phrase):
    # Method 1: Using list
    for (letter) in phrase.split(" "):
        letter = list(letter)
        letter.sort()
        for i in range(len(letter)-1):
            if letter[i] == letter[i+1]:
                return False
    return True

    # Method 2: Using set
    # for letter in phrase.split():
    #     len_letter = len(letter)
    #     len_set = len(set(letter))
    #     if len_letter != len_set:
    #         # Note: set don't have duplicates
    #         # And its duplicate(s) will be deleted
    #         # so its set's length and letter's length will be different if there's a duplicate(s)
    #         return False    # There's duplicate word in letter
    # return True

    # Shorter code:
    # return all(len(set(letter)) == len(letter) for letter in phrase.split())

print(no_duplicate_letters("Fortune favours the bold."))    # Output: True
print(no_duplicate_letters("Look before you leap."))        # Output: False
print(no_duplicate_letters("An apple a day keeps the doctor away."))   # Output: False