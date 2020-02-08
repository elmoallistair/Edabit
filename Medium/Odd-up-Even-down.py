#* Elmo Allistair
#* Written: 08-Dec-2019
#* Published by: Helen Yu
#* Link: https://edabit.com/challenge/ke4FSMdG2XYxbGQny
#* Level: Medium
#* Reference: https://intelligea.wordpress.com/2014/03/19/list-comprehension-with-if-statement-in-python/

#* =======================================================================================

def even_odd_transform(lst, n):
	for i in range(len(lst)):
		for _ in range(n):
			if lst[i] % 2: lst[i] += 2	    # Odd
			else: lst[i] -= 2   # Even
	return lst

    # Shorter code:
    # return [i + n*2 if i%2 else i - n*2 for i in lst]

# Test if it's work
print(even_odd_transform([3, 4, 9], 3))    # Output: [9, -2, 15]
print(even_odd_transform([0, 0, 0], 10))   # Output: [-20, -20, -20]
print(even_odd_transform([1, 2, 3], 1))    # Output: [3, 0, 5]