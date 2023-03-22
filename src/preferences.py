from pysat.formula import CNF
from input import *
from pysatSolve import *
import math
import random
import re


# iterate over the preferences and calculate


# def preferencePenalty(model, preference_penalty):
#     total_penalty = 0
#
#     x = {}
#     x["model"] = model
#     for preference, penalty in preference_penalty.items():
#         variables = preference.split(' OR ')
#         satisfied = False
#         for variable in variables:
#             # check if the variable is negated
#             negated = False
#             if 'Not ' in variable:
#                 variable = variable.split('Not ')[1]
#                 negated = True
#             if 'AND' in variable:
#                 var1, var2 = variable.split(' AND ')
#                 if negated:
#                     satisfied = not ((var1 in model) and (var2 in model))
#                 else:
#                     satisfied = (var1 in model) and (var2 in model)
#             else:
#                 if negated:
#                     satisfied = variable not in model
#                 else:
#                     satisfied = variable in model
#             if satisfied:
#                 break
#         if not satisfied:
#             # the preference is not satisfied, add its penalty to the total
#             total_penalty += penalty
#         preference_penalty_value = penalty if not satisfied else 0
#         x[preference] = preference_penalty_value
#
#     # print the total penalty for the model
#     x["Total"] = total_penalty
#     Penalty.append(x)
#     return Penalty
#
#
# def preferencePossibility(model, preference_possibility):
#     total_tolerance = 0
#     values = []
#     x = {}
#     x["model"] = model
#     for preference, tolerance in preference_possibility.items():
#         variables = preference.split(' OR ')
#         satisfied = False
#         for variable in variables:
#             # check if the variable is negated
#             negated = False
#             if 'Not ' in variable:
#                 variable = variable.split('Not ')[1]
#                 negated = True
#             if 'AND' in variable:
#                 var1, var2 = variable.split(' AND ')
#                 if negated:
#                     satisfied = not ((var1 in model) and (var2 in model))
#                 else:
#                     satisfied = (var1 in model) and (var2 in model)
#             else:
#                 if negated:
#                     satisfied = variable not in model
#                 else:
#                     satisfied = variable in model
#             if satisfied:
#                 break
#
#         # calculate the tolerance for the model for the current preference
#         preference_penalty_value =(1 - tolerance) if not satisfied else 1
#         values.append(preference_penalty_value)
#
#         total_tolerance = min(values)
#         x[preference] = preference_penalty_value
#         # print(f"Tolerance for model '{model}' and preference '{preference}': {preference_penalty_value}")
#
#     # print the total penalty for the model
#     x["Total"] = total_tolerance
#     Possibility.append(x)
#     # print(f"Total tolerance for the model '{model}': {total_tolerance}")
#     # print()
#     return Possibility


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


# def transform(model):
#     clausesV = []
#     # print("model", model[0])
#     if model[0] == "":
#         return 0
#     for pref in model:
#         pref = pref.strip()
#         # split preference string by 'OR'
#         or_tokens = pref.split('OR')
#         # initialize an empty list to store the literals
#         literals = []
#         # iterate over the 'OR' tokens
#         for or_token in or_tokens:
#             # split 'OR' token by 'AND'
#             and_tokens = or_token.split('AND')
#             # initialize a new list of literals for each 'AND' clause
#             and_literals = []
#             # iterate over the 'AND' tokens
#             for and_token in and_tokens:
#                 and_token = and_token.strip()
#                 # check if the token starts with 'NOT'
#                 if and_token.startswith('NOT'):
#                     # get the literal name (without the 'NOT' prefix)
#                     literal = and_token[4:]
#                     # look up the integer value of the literal in the dictionary
#                     value = -original_dict[literal]
#                 else:
#                     # look up the integer value of the literal in the dictionary
#                     value = original_dict[and_token]
#                 # add the literal to the list of AND literals
#                 clausesV.append([value])
#             literals.extend(and_literals)
#         # print(clausesV)
#     return clausesV


def transform(model):
    clausesV = []
    if model[0] == "":
        return 0

    for model in model:
        model = model.strip()
        print(model, 'all')
        # determine if we need to split by "OR" or "AND" first
        if "AND" in model and "OR" in model:
            print(model, 'verified')
            # search for the first occurrence of "OR" and "AND" and check their positions relative to each other
            or_index = model.index("OR")
            and_index = model.index("AND")
            if or_index > and_index:
                # split by "OR" first
                split_tokens = model.split("OR")
                for split_token in split_tokens:
                    # split each sub-expression by "AND"
                    and_tokens = split_token.split("AND")
                    and_literals = []
                    for and_token in and_tokens:
                        and_token = and_token.strip()
                        if and_token.startswith("NOT"):
                            literal = and_token[4:]
                            value = -original_dict[literal]
                        else:
                            value = original_dict[and_token]
                        and_literals.append(value)
                    clausesV.append(and_literals)
            else:
                # split by "AND" first
                split_tokens = model.split("AND")
                for split_token in split_tokens:
                    print(split_token, 'split')
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
                    print(clausesV)
        else:
            if "OR" in model:
                # split by "OR" first
                split_tokens = model.split("OR")
                for split_token in split_tokens:
                    split_token =split_token.strip()
                    if split_token.startswith("NOT"):
                        literal = split_token[4:]
                        value = -original_dict[literal]
                    else:
                        value = original_dict[split_token]
                    # and_literals.append(value)
                    clausesV.append(value)
                clausesV = [clausesV]
                # clausesV.append(and_literals)
                print([clausesV])
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

            # print([clausesV])

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

# optimalPen = t[0]['Total']
#
# for z in t:
#     for f in z:
#         if f["Total"] == optimalPen:
#             print(f['model'])


# def output():
#     for i in n:
#         print(i)
#     return n


# best_set_optimal = set()
# best = math.inf
# cur = 0
# for z in n:
#     cur = 0
#     for key1 in z:
#         if key1 == 'model':
#             print(key1)
#             continue
#         if z[key1] == math.inf:
#             continue
#         cur = cur + z[key1]
#         if cur < best and cur != 0:
#             best = cur
#             best_set_optimal.add(tuple(z['model']))
#         elif cur == best:
#             best_set_optimal.add(tuple(z['model']))


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
