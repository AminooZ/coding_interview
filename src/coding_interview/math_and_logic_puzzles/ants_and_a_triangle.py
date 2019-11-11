# There are three ants on different vertices of a triangle. What is the probability
# of collision (between any two or all of them) if they start walking on the sides of
# the triangle? Assume that each ant randomly picks a direction, with either direction
# being equally likely to be chosen, and that they walk at the same speed.
# Similarly, find the probability of collision with n ants on an n-vertex polygon.


def ants_and_a_triangle(n):
    # 1 - p(all ants go in the same direction: clockwise or anticlockwise)
    return 1 - 2 * (1 / 2) ** n
