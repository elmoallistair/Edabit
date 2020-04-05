# Written: 07-Dec-2019
# https://edabit.com/challenge/BuwHwPvt92yw574zB

def list_of_multiples(num, length):
    num_list = []
    for x in range(1, length+1):
        num_list.append(x*num)
    return num_list
    # return [x*num for x in range(1,length+1)]