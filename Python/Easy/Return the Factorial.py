# Written: 27-Mar-2020
# https://edabit.com/challenge/FF6kYPHdAcJnoosr5

def factorial(num):
	if num == 1:
		return num
	else:
		return num*factorial(num-1)