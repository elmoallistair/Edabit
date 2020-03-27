# Written: 08-Dec-2019
# https://edabit.com/challenge/NNhkGocuPMcryW7GP

def square_areas_difference(r):
    circle_d = 2 * r
    area_big = circle_d ** 2
    area_small = (circle_d/(2**0.5)) ** 2
    difference = int(area_big - area_small)
    return difference
    # return 2 * (r**2)