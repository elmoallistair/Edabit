#* Elmo Allistair
#* Written: 08-Dec-2019
#* Published by: Helen Yu
#* Link: https://edabit.com/challenge/2yHQwkecEHZBfHcmN
#* Level: Medium
#* Reference:
    # https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
    # https://www.programiz.com/python-programming/methods/built-in/len
    # https://www.programiz.com/python-programming/methods/built-in/range

#* =======================================================================================

def progress_days(runs):
    progress = 0
    for days in range(len(runs)-1):
        if runs[days] < runs[days+1]:
            progress += 1
    return progress

    # Shorter code:
    # return len([days for days in range(len(runs)-1) if runs[days] < runs[days+1]])

# Test if it's work
print(progress_days([3, 4, 1, 2]))         # Output: 2
print(progress_days([10, 11, 12, 9, 10]))  # Output: 3
print(progress_days([6, 5, 4, 3, 2, 9]))   # Output: 1
print(progress_days([9, 9]))               # Output: 0