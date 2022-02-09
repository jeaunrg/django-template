from editable.algorithm import ALGO
from editable.questions import QUESTIONS


def add_pbar_nums(algo, i=0):
    new_algo = {}
    if not isinstance(algo, dict):
        return algo, i
    else:
        new_algo = {}
        for k, v in algo.items():
            new_k = k
            if k.split(" %")[0] in QUESTIONS:
                new_k = k + " #" + str(i)
                i += 1
            new_algo[new_k], i = add_pbar_nums(v, i)
        return new_algo, i


def get_algo():
    algo, nums = add_pbar_nums(ALGO)
    return algo, nums
