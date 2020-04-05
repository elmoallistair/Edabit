# Written: 24-Dec-2019
# https://edabit.com/challenge/st8mDxreMcuWxuz8c

def pentagonal(num):
    if num == 1:
        return num
    else:
        return (num-1)*5 + pentagonal(num-1)
    # return int(1 + num * (num-1) * (5/2))