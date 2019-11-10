# You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of
# weight 1.1 grams. Given a scale that provides an exact measurement, how would you
# find the heavy bottle. You can only use the scale once.


def set_heavy_pill(heavy_pill=1):
    def get_weight(pills):
        weight = 0
        for pill, number in pills.items():
            if pill == heavy_pill:
                weight += number * 1.1
            else:
                weight += number * 1.0
        return weight

    return get_weight


def the_heavy_pill(get_weight_fn=set_heavy_pill(heavy_pill=1)):
    pills = {i + 1: i + 1 for i in range(20)}
    weight = get_weight_fn(pills=pills)
    return round(10 * (weight - 20 * 21 / 2))
