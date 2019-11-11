# You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test strips
# which can be used to detect poison. A single drop of poison will turn the test strip
# positive permanently. You can put any number of drops on a test strip at once and can
# reuse a test strip as many times as you'd like (as long as the results are negative).
# However, you can only run tests once per day and it takes 7 days to return the result.
# How would you figure out the poisoned bottle in as few days as possible ?
# Follow up: Write code to simulate your approach.


def set_poisoned_bottle(bottle):
    def test_strip(bottles):
        if bottle in bottles:
            return 1
        return 0

    return test_strip


def int_to_binary(number, size):
    return format(number, 'b').zfill(size)


def poison(test_strip_fn):
    strips = [[] for _ in range(10)]
    for bottle in range(1000):
        binary_bottle = int_to_binary(bottle, 10)
        for index in range(10):
            if binary_bottle[index] == '1':
                strips[index].append(bottle)
    return int(''.join([str(test_strip_fn(strip)) for strip in strips]), 2)
