#* Perfect Square Patch
#* Instructions: Create a function that takes an integer and outputs an n x n square solely consisting of the integer n.
#* Published by: Helen Yu
#* Link: https://edabit.com/challenge/K3qMssK6mF34ctXE5
#* Level: Medium

#* Elmo Allistair
#* Written: 08-12-2019
#* Reference:
    # https://www.programiz.com/python-programming/methods/list/append
    # https://www.programiz.com/python-programming/list-comprehension

#* =======================================================================================

def square_patch(n):
    arr = []
    for _ in range(n):
        arr.append([n for j in range(n)])
    return arr

    # Shorter code:
    # return [[n]*n]*n

# Test if it's work
print(square_patch(3))  # Output: [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
print(square_patch(5))  # Output: [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
print(square_patch(1))  # Output: [[1]]
print(square_patch(0))  # Output: []