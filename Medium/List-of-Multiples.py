# Written: 07-Dec-2019
'''
* Instructions:
*   Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.
*
*   Examples
*     list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
*     list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
*     list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]
*
*   Notes
*     Notice that num is also included in the returned list.
*
* Resources:
*   - https://python-textbok.readthedocs.io/en/1.0/Collections.html?highlight=join#ranges
*   - https://python-textbok.readthedocs.io/en/1.0/Loop_Control_Statements.html?highlight=loop#the-for-statement
*   - https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
'''

# =======================================================================================

def list_of_multiples(num, length):
    num_list = []
    for x in range(1, length+1):
        num_list.append(x*num)
    return num_list

    # return [x*num for x in range(1,length+1)]

print(list_of_multiples(7,5))      # Output: [7, 14, 21, 28, 35]
print(list_of_multiples(12,10))    # Output: [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
print(list_of_multiples(17,6))     # Output: [17, 34, 51, 68, 85, 102]