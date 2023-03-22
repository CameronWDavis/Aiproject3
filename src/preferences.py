from pysat.formula import CNF
from input import *
from pysatSolve import *
import math
import random
import re


# iterate over the preferences and calculate

def preferencePenalty(model, preference_penalty, modelV):
    total_penalty = 0
    x = {}
    x["model"] = modelV
    for preference, penalty in preference_penalty.items():
        print(transform([preference]))
        if not solve(model, transform([preference])):
            preference_penalty_value = penalty
            total_penalty += penalty
        else:
            preference_penalty_value = 0

        x[preference] = preference_penalty_value

    # print the total penalty for the model
    x["Total"] = total_penalty
    Penalty.append(x)
    return Penalty


def preferencePossibility(model, preference_possibility, modelV):
    total_tolerance = 0
    values = []
    x = {}
    x["model"] = modelV
    for preference, tolerance in preference_possibility.items():
        print(preference)
        if not solve(model, transform([preference])):
            preference_penalty_value = (1 - tolerance)
            values.append(preference_penalty_value)
        else:
            preference_penalty_value = 1
            values.append(preference_penalty_value)

        x[preference] = preference_penalty_value
        total_tolerance = min(values)

    x["Total"] = total_tolerance
    Possibility.append(x)
    return Possibility


def preferenceQualitative(model, preference_qualitative, modelV):
    # satisfaction = math.inf
    x = {}
    x["model"] = modelV

    for items in preference_qualitative:
        v = items["preference"]
        for preference in items["preference"]:
            conditionNow = items["condition"]
            # print("conditionNow", conditionNow[0])
            # print(solve(model, transform(conditionNow)))

            x[items["statement"]] = math.inf
            if solve(model, transform(conditionNow)):
                if solve(model, transform(preference)):
                    satisfaction = items["preference"].index(preference) + 1

                    x[items["statement"]] = satisfaction
                    break
    Qualitative.append(x)
    return Qualitative


def transform(model):
    clausesV = []
    if model[0] == "":
        return 0

    for model in model:
        model = model.strip()
        print(model, 'all')
        # determine if "OR" or "AND" are inside the model
        if "AND" in model and "OR" in model:
            # split by "AND" first
            split_tokens = model.split("AND")
            for split_token in split_tokens:
                # print(split_token, 'split')
                # split each sub-expression by "OR"
                or_tokens = split_token.split("OR")
                or_literals = []
                for or_token in or_tokens:
                    or_token = or_token.strip()
                    if or_token.startswith("NOT"):
                        literal = or_token[4:]
                        value = -original_dict[literal]
                    else:
                        value = original_dict[or_token]
                    or_literals.append(value)
                clausesV.append(or_literals)
                print(clausesV, 'AND break')
        else:
            if "OR" in model:
                # split by "OR" first
                split_tokens = model.split("OR")
                for split_token in split_tokens:
                    split_token = split_token.strip()
                    if split_token.startswith("NOT"):
                        literal = split_token[4:]
                        value = -original_dict[literal]
                    else:
                        value = original_dict[split_token]
                    # and_literals.append(value)
                    clausesV.append(value)
                clausesV = [clausesV]
                # clausesV.append(and_literals)
                print(clausesV)
            else:
                # split each expression  by "AND"
                and_tokens = model.split("AND")
                and_literals = []
                for and_token in and_tokens:
                    and_token = and_token.strip()
                    if and_token.startswith("NOT"):
                        literal = and_token[4:]
                        value = -original_dict[literal]
                    else:
                        value = original_dict[and_token]
                    # and_literals.append(value)
                    clausesV.append([value])
            # clausesV = [clausesV]

            print(clausesV)

    return clausesV


# list containing all the model and the different penalty logic base on the preferences
Penalty = []
# list containing all the model and the different possibility logic base on the preferences
Possibility = []
# list containing all the model and the different qualitative logic base on the preferences
Qualitative = []

# for model in models:
#     t_normal = preferencePenalty(model, preferencesPenalty)
#
# for model in models:
#     k_normal = preferencePossibility(model, preferencesPossibility)
for x, y in zip(models, modelsCNF):
    t_normal = preferencePenalty(y, preferencesPenalty, x)

for x, y in zip(models, modelsCNF):
    k_normal = preferencePossibility(y, preferencesPossibility, x)

for x, y in zip(models, modelsCNF):
    n = preferenceQualitative(y, preferencesQualitative, x)

# print()
print("Preference : Penalty Logic")
# sorted the list with respect to the Total penalty: assending
t = sorted(t_normal, key=lambda x: x['Total'], reverse=False)
# print(t)

print()
print("Preference : Possibility Logic")
k = sorted(k_normal, key=lambda x: x['Total'], reverse=True)
# print(k)

print()
print("Preference : Qualitative Logic")
# # n = sorted(n, key=lambda x: x['Total'], reverse=False)
# print(n)

# print()
# print("Preference : Penalty Logic")
# for i in t:
#     print(i)
# print()
# print("Preference : Possibility Logic")
for i in k:
    print(i)
print()
print("Preference : Qualitative Logic")
for i in n:
    print(i)

# exemplification tow random feasible object
s = random.sample(models, 2)
#
# print(s)
print()
for z in t:
    for f in t:
        if z["model"] == s[0] and f['model'] == s[1]:
            if z["Total"] < f["Total"]:
                print(f"{s[0]} is preferred to {s[1]} according to penalty Logic.")
            elif z["Total"] > f["Total"]:
                print(f"{s[1]} is preferred to {s[0]} according to penalty Logic.")
            else:
                print(f"{s[0]} is equally preferred to {s[1]} according to penalty Logic.", z["Total"], f["Total"])

print()

for z in k:
    for f in k:
        if z["model"] == s[0] and f['model'] == s[1]:
            if z["Total"] > f["Total"]:
                print(f"{s[0]} is preferred to {s[1]} according to possibilistic Logic.")
            elif z["Total"] < f["Total"]:
                print(f"{s[1]} is preferred to {s[0]} according to possibilistic Logic.")
            else:
                print(f"{s[0]} is equally preferred to {s[1]} according to possibilistic Logic.", z["Total"],
                      f["Total"])

print()

val1, val2 = 0, 0
for z in n:
    for f in n:
        if z["model"] == s[0] and f['model'] == s[1]:
            for key1, key2 in zip(z, f):
                # Skip the 'model' key since we already printed its value
                if key1 == 'model' or key2 == 'model':
                    continue
                if z[key1] == math.inf and f[key2] == math.inf:
                    continue
                if z[key1] != math.inf and f[key2] == math.inf:
                    val1 += 1
                if z[key1] == math.inf and f[key2] != math.inf:
                    val2 += 1
                if z[key1] < f[key2]:
                    val1 += 1
                if z[key1] > f[key2]:
                    val2 += 1

if val1 < val2:
    print(f"{s[1]} is preferred to {s[0]} according to qualitative Logic.")
elif val1 > val2:
    print(f"{s[0]} is preferred to {s[1]} according to qualitative Logic.")
elif val1 == val2:
    print(f"{s[0]} is equally preferred to {s[1]} according to qualitative Logic.", val1, val2)
else:
    print(f"{s[0]} and {s[1]} are incomparable according to qualitative Logic.")

print()

print(f"The optimal object according to penalty Logic is {t[0]['model']}")
print()
print(f"The optimal object according to penalty possibilistic is {t[0]['model']}")
print()


# val1, val2 = 0, 0
best_set_optimal = set()

# for z in n:
z = n[0]
for f in n:
    val2 = 0
    val1 = 0
    for key1, key2 in zip(z, f):
        # Skip the 'model' key since we already printed its value
        if key1 == 'model' or key2 == 'model':
            continue
        if z[key1] == math.inf and f[key2] == math.inf:
            continue
        if z[key1] != math.inf and f[key2] == math.inf:
            val1 += 1
        if z[key1] == math.inf and f[key2] != math.inf:
            val2 += 1
        if z[key1] < f[key2]:
            val1 += 1
        if z[key1] > f[key2]:
            val2 += 1
    print(val1, val2, "current values")
    if val1 > val2:
        best_set_optimal.add(tuple(z['model']))
    elif val1 < val2:
        best_set_optimal.add(tuple(f['model']))
        z = f
    else:
        best_set_optimal.add(tuple(z['model']))
        best_set_optimal.add(tuple(f['model']))
    val1 = 0
    val2 = 0

print("bestset", best_set_optimal)
