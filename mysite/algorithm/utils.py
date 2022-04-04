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


def algo_to_dict(df, n_questions=0):
    d = {}
    indexes = np.where(df.iloc[:, 0].notnull())[0]
    for i, ind in enumerate(indexes):
        key = str(df.iloc[ind, 0])
        if key.startswith("Q:"):
            key = key.split(":")[1] + " #" + str(n_questions)
            n_questions += 1
        if str(df.iloc[ind, 1]) != "nan":
            d[key] = str(df.iloc[ind, 1])
        else:
            if ind == indexes[-1]:
                sub_df = df.iloc[ind + 1 :, 1:]
            else:
                sub_df = df.iloc[ind + 1 : indexes[i + 1], 1:]
            d[key], n_questions = algo_to_dict(sub_df, n_questions)
    return d, n_questions


def question_to_dict(df):
    d = defaultdict(dict)
    for ind in df.index:
        d[ind]["question"] = df.loc[ind, "question"]
        d[ind]["answers"] = list(df.loc[ind].dropna()[1:])
    return dict(d)


def reference_to_dict(df):
    df = df[df.index.notnull()]
    ref_dict = dict()
    for ref in df.index:
        d = defaultdict(list)
        for colname in df.columns:
            value = df.loc[ref, colname]
            if isinstance(value, str):
                if colname in ["description", "pathologie"]:
                    d[colname] = value
                else:
                    d["traitement"].append(value)
        ref_dict[str(int(ref))] = dict(d)
    return ref_dict