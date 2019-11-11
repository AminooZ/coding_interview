# There is a building of 100 floors. If an egg drops from the nth floor or above, it
# will break. If it's dropped from any floor below, it will not break. You're given
# two eggs. Find n, while minimizing the number of drops for the worst case.


def set_floor(n):
    def get_egg_state(floor):
        if floor >= n:
            return True
        return False

    return get_egg_state


def the_egg_drop_problem(floors_count, get_egg_state_fn):
    floor, step = 0, 0
    while floor <= floors_count:
        step += 1
        floor += step
    floor_egg_1 = step
    while floor_egg_1 <= floors_count and not get_egg_state_fn(floor=floor_egg_1):
        floor_egg_1 += step
        step -= 1
    floor_egg_2 = floor_egg_1 - step
    while floor_egg_2 <= floor_egg_1 and not get_egg_state_fn(floor=floor_egg_2):
        floor_egg_2 += 1
    return floor_egg_2
