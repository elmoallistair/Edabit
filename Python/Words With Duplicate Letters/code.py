# Written: 12-Dec-2019
# https://edabit.com/challenge/WS6hR6b9EZzuDTD26

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