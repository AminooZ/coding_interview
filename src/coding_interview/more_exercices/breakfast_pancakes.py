# Introduction:
# At the Infinite House of Pancakes, there are only finitely many pancakes, but there
# are infinitely many diners who would be willing to eat them! When the restaurant
# opens for breakfast, among the infinitely many diners, exactly D have non-empty
# plates; the ith of these has Pi pancakes on his or her plate. Everyone else has an
# empty plate. Normally, every minute, every diner with a non-empty plate will eat one
# pancake from his or her plate.
# Special minutes:
# Some minutes may be special. In a special minute, the head server asks for the
# diners’s attention, chooses a diner with a non-empty plate, and carefully lifts some
# number of pancakes off of that diner’s plate and moves those pancakes onto one other
# diner’s (empty or non-empty) plate. No diners eat during a special minute, because it
# would be rude.
# Your job :
# You are the head server on duty this morning, and it is your job to decide which
# minutes, if any, will be special, and which pancakes will move where. That is,
# every minute, you can decide to either do nothing and let the diners eat, or declare
# a special minute and interrupt the diners to make a single movement of one or more
# pancakes, as described above.
# Breakfast ends when there are no more pancakes left to eat. How quickly can you make
# that happen?
# Your mission:
# Your real job as an engineer now is to code the function get_minimum_finish_time
# that returns the minimum number of minutes to finish all the pancakes.
# Your input:
# Your input is a list of positive integers. The ith element of your list represents
# the number of pancakes on a diner’s plate.
# Example: The list [2, 4, 5] represents 3 diners with respectively 2, 4 and 5 pancakes.
# The rest of diners (infinite) have empty plates.
from math import ceil


def regular_minute(non_empty_plates):
    return [x - 1 for x in non_empty_plates if x > 0]


def special_minute(non_empty_plates, source_plate, destination_plate, nb_pancakes):
    assert 0 <= source_plate < len(non_empty_plates), \
        f'Source plate {source_plate} is empty'
    assert non_empty_plates[source_plate] >= nb_pancakes, \
        f'Source plate {source_plate} contains {non_empty_plates[source_plate]} ' \
            f'but {nb_pancakes} were requested'
    non_empty_plates[source_plate] -= nb_pancakes
    if 0 <= destination_plate < len(non_empty_plates):
        non_empty_plates[destination_plate] += nb_pancakes
    else:
        non_empty_plates.append(nb_pancakes)
    return non_empty_plates


def get_minimum_to_target(non_empty_plates, target):
    return sum([1 for x in non_empty_plates if x > target])


def get_minimum_finish_time(non_empty_plates, verbose=False):
    consumed_steps = 0
    maximum = max(non_empty_plates)
    target = ceil(maximum / 2)
    steps_to_target = get_minimum_to_target(
        non_empty_plates=non_empty_plates,
        target=target
    )
    if verbose:
        print(non_empty_plates)
    while maximum - steps_to_target >= target and maximum > 1:
        if verbose:
            print(f'special minute x {steps_to_target}')
        for _ in range(steps_to_target):
            non_empty_plates = special_minute(
                non_empty_plates=non_empty_plates,
                source_plate=non_empty_plates.index(maximum),
                destination_plate=-1,
                nb_pancakes=ceil(maximum / 2)
            )
            if verbose:
                print(non_empty_plates)
        consumed_steps += steps_to_target
        maximum = max(non_empty_plates)
        target = ceil(maximum / 2)
        steps_to_target = get_minimum_to_target(
            non_empty_plates=non_empty_plates,
            target=target
        )
    if verbose:
        print(f'regular minute x {maximum}')
        for x in range(maximum):
            non_empty_plates = regular_minute(non_empty_plates=non_empty_plates)
            print(non_empty_plates)
    return consumed_steps + maximum
