# Written: 23-Dec-2019
# https://edabit.com/challenge/pQavNkBbdmvSMmx5x

def majority_vote(lst):
    N = len(lst)/2
    for choice in set(lst):
        if lst.count(choice) > N:
            return choice