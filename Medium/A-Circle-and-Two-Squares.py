# Written: 08-Dec-2019
'''
* Instructions:
*   Imagine a circle and two squares: a smaller and a bigger one.
*   For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.
*
*   Create a function, that takes an integer (radius of the circle) and returns the difference of the square-areas.
*
*   Examples
*     square_areas_difference(5) ->➞ 50
*     square_areas_difference(6) ->➞ 72
*     square_areas_difference(7) ->➞ 98
*
*   Notes
*     Use only positive integer parameters.
*
* Resources:
*   - https://www.dummies.com/education/math/calculus/how-to-work-with-45-45-90-degree-triangles/
*   - http://www.cut-the-knot.org/triangle/EulerIO.shtml
'''

# =======================================================================================

def square_areas_difference(r):
    circle_d = 2 * r
    area_big = circle_d ** 2
    area_small = (circle_d/(2**0.5)) ** 2
    difference = int(area_big - area_small)
    return difference

    # return 2 * (r**2)

print(square_areas_difference(5))  # Output: 50
print(square_areas_difference(6))  # Output: 72
print(square_areas_difference(7))  # Output: 98