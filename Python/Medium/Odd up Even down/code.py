# Written: 08-Dec-2019
# https://edabit.com/challenge/ke4FSMdG2XYxbGQny

def even_odd_transform(lst, n):
	for i in range(len(lst)):
		for _ in range(n):
			if lst[i] % 2: lst[i] += 2
			else: lst[i] -= 2
	return lst
	# return [i + n*2 if i%2 else i - n*2 for i in lst]