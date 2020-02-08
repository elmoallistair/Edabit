# Written: 07-12-2019
'''
* Instructions:
*   Suppose you have a guest list of students and the country they are from, stored as key-value pairs in a dictionary.
*     GUEST_LIST = {
*     "Randy": "Germany",
*     "Karla": "France",
*     "Wendy": "Japan",
*     "Norman": "England",
*     "Sam": "Argentina"
*     }
*
*   Write a function that takes in a name and returns a name tag, that should read:
*     "Hi! I'm [name], and I'm from [country]."
*
*   If the name is not in the dictionary, return:
*     "Hi! I'm a guest."
*
*   Examples
*     greeting("Randy") ➞ "Hi! I'm Randy, and I'm from Germany."
*     greeting("Sam") ➞ "Hi! I'm Sam, and I'm from Argentina."
*     greeting("Monti") ➞ "Hi! I'm a guest."
*
*   Notes
*     N/A
*
* Resources:
*   - https://www.tutorialspoint.com/python/dictionary_get.htm
*   - https://stackoverflow.com/questions/43488137/how-to-do-a-dictionary-format-with-f-string-in-python-3-6
'''

# =======================================================================================

def greeting(name):
    for i in GUEST_LIST:
        if i.lower() == name.lower():
            return "Hi! I'm {}, and I'm from {}.".format(i,GUEST_LIST[i])
    else: return "Hi! I'm a guest."

GUEST_LIST = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina"
}

print(greeting("Randy"))    # Output: Hi! I'm Randy, and I'm from Germany.
print(greeting("Sam"))      # Output: Hi! I'm Sam, and I'm from Argentina.
print(greeting("Monti"))    # Output: Hi! I'm a guest.