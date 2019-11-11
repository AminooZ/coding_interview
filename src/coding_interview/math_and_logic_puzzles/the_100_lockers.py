# There 100 closed lockers in a hallway. A man begins by opening all 100 lockers.
# Next, he closes every second locker. Then on his third pass he toggles every third
# locker (closes it if it is open or opens it if it is closed). This process continues
# for 100 passes, such that on each pass i, the ma toggles every ith locker. After the
# 100 pass in the hallway, in which he toggles only locker #100, how many lockers are
# open ?
from math import sqrt

from bitarray import bitarray


def get_prime_numbers_under_100():
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97]


def get_divisors(number):
    divisors = []
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            divisors.append(i)
    divisors.append(number)
    return divisors


def is_square_number(number):
    return int(sqrt(number)) == sqrt(number)


def prime_decomposition(number, get_prime_numbers_fn=get_prime_numbers_under_100):
    prime_numbers = get_prime_numbers_fn()
    decomposition = []
    index = -1
    prime_number = prime_numbers[0]
    while number >= prime_number and index < len(prime_numbers):
        index += 1
        prime_number = prime_numbers[index]
        while number % prime_number == 0:
            number //= prime_number
            decomposition.append(prime_number)
    return decomposition


def the_100_lockers():
    open_lockers = 0
    for locker_i in range(1, 101):
        #  only square numbers have an odd number of divisors
        open_lockers += is_square_number(number=locker_i)
    return open_lockers


def the_100_lockers_less_naive():
    open_lockers = 0
    for locker_i in range(1, 101):
        open_lockers += len(get_divisors(number=locker_i)) % 2 == 1
    return open_lockers


def the_100_lockers_naive():
    lockers = bitarray(100)
    lockers.setall(1)  # 1 is open
    for pass_i in range(2, 101):
        for i in range(pass_i, 101, pass_i):
            lockers[i - 1] = not lockers[i - 1]
    return sum(lockers)
