# Written: 07-Dec-2019
'''
* Instructions:
*   Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
*   - If the number is a multiple of 3 the output should be "Fizz".
*   - If the number given is a multiple of 5, the output should be "Buzz".
*   - If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
*   - If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
*
*   Examples
*     fizz_buzz(3) ->➞ "Fizz"
*     fizz_buzz(5) ->➞ "Buzz"
*     fizz_buzz(15) ->➞ "FizzBuzz"
*     fizz_buzz(4) ->➞ "4"
*
*   Notes
*   - Try to be precise with how you spell things and where you put the capital letters.
*   - If you get stuck on a challenge, find help in the Resources tab.
*   - If you're really stuck, unlock solutions in the Solutions tab.
*
* Resources:
*   - https://medium.com/@GalarnykMichael/python-basics-8-fizzbuzz-441e97c6c767
*   - https://stackoverflow.com/questions/8002217/how-do-you-check-whether-a-number-is-divisible-by-another-number-python
'''

# =======================================================================================

def fizz_buzz(num):
	if (num % 3 == 0) and (num % 5 == 0): return "FizzBuzz"
	elif num % 3 == 0: return "Fizz"
	elif num % 5 == 0: return "Buzz"
	else: return str(num)

print(fizz_buzz(3))     # Output: Fizz
print(fizz_buzz(5))     # Output: Buzz
print(fizz_buzz(15))    # Output: FizzBuzz
print(fizz_buzz(4))     # Output: 4