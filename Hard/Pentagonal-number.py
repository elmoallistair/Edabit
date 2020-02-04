# Written: 24-Dec-2019
'''
* Instructions:
*  Write a function that takes a positive integer and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.
*
*  In the image below you can see the first iteration is only a single dot.
*  On the second, there are 6 dots. On the third, there are 16 dots, and on the fourth there are 31 dots.
*
*  Return the number of dots that exist in the whole pentagon on the Nth iteration.
*
*  Examples
*    pentagonal(1) ->➞ 1
*    pentagonal(2) ->➞ 6
*    pentagonal(3) ->➞ 16
*    pentagonal(8) ->➞ 141
*
*  Notes
*    N/A
*
* Resources: http://mathworld.wolfram.com/PentagonalNumber.html
'''

# =======================================================================================

def pentagonal(num):
    if num == 1:
        return num
    else:
        return (num-1)*5 + pentagonal(num-1)

    # return int(1 + num * (num-1) * (5/2))


print(pentagonal(1))   # Output: 1
print(pentagonal(2))   # Output: 6
print(pentagonal(3))   # Output: 16
print(pentagonal(8))   # Output: 141