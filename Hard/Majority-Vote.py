# Written: 23-Dec-2019
'''
* Instructions:
*   Create a function that returns the majority vote in a list.
*   A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
*
*   Examples
*     majority_vote(["A", "A", "B"]) ->➞ "A"
*     majority_vote(["A", "A", "A", "B", "C", "A"]) ->➞ "A"
*     majority_vote(["A", "B", "B", "A", "C", "C"]) ->➞ None
*
*   Notes
*     - The frequency of the majority element must be strictly greater than 1/2.
*     - If there is no majority element, return None.
*     - If the list is empty, return None.
*
* Resources:
*   - https://www.geeksforgeeks.org/majority-element/
*   - https://www.programiz.com/python-programming/methods/list/count
*   - https://stackoverflow.com/questions/15181867/understanding-the-set-function
'''

# =======================================================================================

def majority_vote(lst):
    if not lst:
        return None         # If the list is empty, return None.
    raw_choice = set(lst)
    N = len(lst)/2
    for choice in raw_choice:
        if (lst.count(choice)) > N:
            return choice   # A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
    return None             # If there is no majority element, return None.

    # Shorter Code:
    # N = len(lst)/2
    # for choice in set(lst):
    #     if lst.count(choice) > N:
    #         return choice


print(majority_vote([]))
print(majority_vote(["A", "A", "B"]))                 # Output: "A"
print(majority_vote(["A", "A", "A", "B", "C", "A"]))  # Output: "A"
print(majority_vote(["A", "B", "B", "A", "C", "C"]))  # Output: None