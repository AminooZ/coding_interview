# In the new post-apocalyptic world, the world queen is desperately concerned about the
# birth rate. Therefore, she decrees that all families should ensure that they have one
# girl or else they face massive fines. If all families abide by the policy, that is,
# they continue to have children until they have one girl, at which point they
# immediately stop. What will the gender ratio of the new generation be ?
# Assume that the odds of someone having a boy or a girl on any given pregnancy is
# equal.
# Solve this out logically and then write a computer simulation of it.
from random import uniform


def set_gender_probability(boy_probability):
    def get_gender():
        if uniform(0, 1) <= boy_probability:
            return 'B'
        return 'G'

    return get_gender


def the_apocalypse(families_count,
                   get_gender_fn=set_gender_probability(boy_probability=0.5)):
    boys_count = 0
    for _ in range(families_count):
        while get_gender_fn() == 'B':
            boys_count += 1
    return boys_count / (families_count + boys_count)
