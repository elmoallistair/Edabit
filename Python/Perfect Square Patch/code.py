# Written: 08-12-2019
# https://edabit.com/challenge/K3qMssK6mF34ctXE5

def square_patch(n):
    arr = []
    for _ in range(n):
        arr.append([n for j in range(n)])
    return arr
    # return [[n]*n]*n