# Written: 23-Dec-2019
# https://edabit.com/challenge/ehyZvt6AJF4rKFfXT

def uncensor(txt, vowels):
    new_txt = []            # Storing new (uncencored) text
    vowels = list(vowels)   # Convert vowels to list
    j = 0                   # Start index for vowels list
    for i in txt:           # Loop over txt
        if i == '*':
            new_txt.append(vowels[j])   # change '*' to current index of vowels
            j+=1
            continue                    # skip the rest of code for current iteration
        new_txt.append(i)
    return ''.join(new_txt)             # returns a string from new_txt list

    # Shorter Code:
    # vowels = list(vowels)   # Convert vowels to list
    # return ''.join([vowels.pop(0) if i=='*' else i for i in txt])