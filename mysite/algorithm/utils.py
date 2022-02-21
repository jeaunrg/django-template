from collections import defaultdict

import numpy as np
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


def dftree_to_dict(df):
    d = {}
    indexes = np.where(df.iloc[:, 0].notnull())[0]
    for i, ind in enumerate(indexes):
        key = str(df.iloc[ind, 0])
        if key.startswith("Q:"):
            key = key[2:]
        if str(df.iloc[ind, 1]) != "nan":
            d[key] = str(df.iloc[ind, 1])
        else:
            if ind == indexes[-1]:
                d[key] = dftree_to_dict(df.iloc[ind + 1 :, 1:])
            else:
                d[key] = dftree_to_dict(df.iloc[ind + 1 : indexes[i + 1], 1:])
    return d


def dfq_to_dict(df):
    d = defaultdict(dict)
    for ind in df.index:
        d[ind]["question"] = df.loc[ind, "question"]
        d[ind]["answers"] = list(df.loc[ind].dropna()[1:])
    return dict(d)
