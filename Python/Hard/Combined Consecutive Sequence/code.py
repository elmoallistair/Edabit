# Written: 05-Apr-2020
# https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb

def consecutive_combo(lst1, lst2):
    lst = lst1+lst2
    temp = [i for i in range(min(lst), max(lst)+1)]

    return sorted(lst) == temp