# Written: 07-Dec-2019
# https://edabit.com/challenge/o2AKq4xy3nfZabKXL

def solutions(a, b, c):
    D = b**2 - (4*a*c)
    if D < 0: return 0
    elif D == 0: return 1
    elif D > 0: return 2