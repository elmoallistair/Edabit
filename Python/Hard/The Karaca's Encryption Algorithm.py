# Written: 09-Dec-2019
# https://edabit.com/challenge/JzBLDzrcGCzDjkk5n

def encrypt(word):
    word = (word[::-1]).lower()
    trans = word.replace('a', '0').replace('e', '1').replace('o','2').replace('u','3')
    return trans+'aca'
    # return word[::-1].translate(str.maketrans('aeou', '0123')) + 'aca'