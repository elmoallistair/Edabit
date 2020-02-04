# Written: 23-Dec-2019
'''
* Instructions:
*   Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s.
*   Luckily, I've been able to find the vowels that were removed.
*
*   Given a censored string and a string of the censored vowels, return the original uncensored string.
*
*   Example
*     uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ->➞ "Where did my vowels go?"
*     uncensor("abcd", "") ->➞ "abcd"
*     uncensor("*PP*RC*S*", "UEAE") ->➞ "UPPERCASE"
*
*   Notes
*     - The vowels are given in the correct order.
*     - The number of vowels will match the number of * characters in the censored string.
*
* Resources:
*   - https://www.w3schools.com/python/ref_string_format.asp
*   - https://www.w3schools.com/python/ref_string_replace.asp
'''

# =======================================================================================

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

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))    # Output: "Where did my vowels go?"
print(uncensor("abcd", ""))                             # Output: "abcd"
print(uncensor("*PP*RC*S*", "UEAE"))                    # Output: "UPPERCASE"