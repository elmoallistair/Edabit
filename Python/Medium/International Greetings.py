# Written: 07-12-2019
# https://edabit.com/challenge/vAS4Hp4wzSEnQs3tZ

GUEST_LIST = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina"
}

def greeting(name):
    for i in GUEST_LIST:
        if i.lower() == name.lower():
            return "Hi! I'm {}, and I'm from {}.".format(i,GUEST_LIST[i])
    else: return "Hi! I'm a guest."

