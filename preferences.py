from pysat.solvers import Glucose3
from pysat.formula import CNF
from input import *
from pysatSolve import *
import math
import random
import re
import pandas as pd


# iterate over the preferences and calculate


def preferencePenalty(model, preference_penalty):
    total_penalty = 0

    x = {}
    x["model"] = model
    for preference, penalty in preference_penalty.items():
        variables = preference.split(' OR ')
        satisfied = False
        for variable in variables:
            # check if the variable is negated
            negated = False
            if 'Not ' in variable:
                variable = variable.split('Not ')[1]
                negated = True
            if 'AND' in variable:
                var1, var2 = variable.split(' AND ')
                if negated:
                    satisfied = not ((var1 in model) and (var2 in model))
                else:
                    satisfied = (var1 in model) and (var2 in model)
            else:
                if negated:
                    satisfied = variable not in model
                else:
                    satisfied = variable in model
            if satisfied:
                break
        if not satisfied:
            # the preference is not satisfied, add its penalty to the total
            total_penalty += penalty

        # calculate the penalty for the model for the current preference
        preference_penalty_value = penalty if not satisfied else 0
        # '0'f"{to_subscript(assign_binary(y))}"
        # x = {"model": model, preference: preference_penalty}
        x[preference] = preference_penalty_value
        # print(f"Penalty for model '{model}' and preference '{preference}': {preference_penalty_value}")

    # print the total penalty for the model
    x["Total"] = total_penalty
    Penalty.append(x)
    # print(f"Total penalty for the model '{model}': {total_penalty}")
    # print()
    return Penalty


def preferencePossibility(model, preference_possibility):
    total_tolerance = 0
    values = []
    x = {}
    x["model"] = model
    for preference, tolerance in preference_possibility.items():
        variables = preference.split(' OR ')
        satisfied = False
        for variable in variables:
            # check if the variable is negated
            negated = False
            if 'Not ' in variable:
                variable = variable.split('Not ')[1]
                negated = True
            if 'AND' in variable:
                var1, var2 = variable.split(' AND ')
                if negated:
                    satisfied = not ((var1 in model) and (var2 in model))
                else:
                    satisfied = (var1 in model) and (var2 in model)
            else:
                if negated:
                    satisfied = variable not in model
                else:
                    satisfied = variable in model
            if satisfied:
                break

        # calculate the tolerance for the model for the current preference
        preference_penalty_value = (1 - tolerance) if not satisfied else 1
        values.append(preference_penalty_value)

        total_tolerance = min(values)
        x[preference] = preference_penalty_value
        # print(f"Tolerance for model '{model}' and preference '{preference}': {preference_penalty_value}")

    # print the total penalty for the model
    x["Total"] = total_tolerance
    Possibility.append(x)
    # print(f"Total tolerance for the model '{model}': {total_tolerance}")
    # print()
    return Possibility


def preferenceQualitative(model, preference_qualitative, modelV, ):
    satisfaction = math.inf
    x = {}
    x["model"] = modelV

    for items in preference_qualitative:
        v = items["preference"]
        for preference in items["preference"]:
            conditionNow = items["condition"]
            if not solve(model, transform(conditionNow)):
                # v = items["preference"]
                break

            if solve(model, transform(preference)):
                satisfaction = items["preference"].index(preference) + 1
            # print(
            #     f"Satisfaction for model O{to_subscript(assign_binary(model))} and preference '{preference}' and condition {conditionNow}: {satisfaction}")
        x[items["statement"]] = satisfaction
    Qualitative.append(x)
    # print(
    #     f"Satisfaction for model O{to_subscript(assign_binary(model))} and preference '{preference}' and condition {conditionNow}: {satisfaction}")
    # print(
    #     f"Satisfaction for model O{to_subscript(assign_binary(model))} and preference '{v}' and condition {conditionNow}: {satisfaction}")
    return Qualitative


def transform(model):
    clausesV = []
    for pref in model:
        pref = pref.strip()
        # split preference string by 'OR'
        or_tokens = pref.split('OR')
        # initialize an empty list to store the literals
        literals = []
        # iterate over the 'OR' tokens
        for or_token in or_tokens:
            # split 'OR' token by 'AND'
            and_tokens = or_token.split('AND')
            # initialize a new list of literals for each 'AND' clause
            and_literals = []
            # iterate over the 'AND' tokens
            for and_token in and_tokens:
                and_token = and_token.strip()
                # check if the token starts with 'NOT'
                if and_token.startswith('NOT'):
                    # get the literal name (without the 'NOT' prefix)
                    literal = and_token[4:]
                    # look up the integer value of the literal in the dictionary
                    value = -original_dict[literal]
                else:
                    # look up the integer value of the literal in the dictionary
                    value = original_dict[and_token]
                # add the literal to the list of AND literals
                clausesV.append([value])
            literals.extend(and_literals)
        # print(clausesV)
    return clausesV





# list containing all the model and the different penalty logic base on the preferences
Penalty = []
# list containing all the model and the different possibility logic base on the preferences
Possibility = []
# list containing all the model and the different qualitative logic base on the preferences
Qualitative = []

for model in models:
    t = preferencePenalty(model, preferencesPenalty)

for model in models:
    k = preferencePossibility(model, preferencesPossibility)

for x, y in zip(models, modelsCNF):
    n = preferenceQualitative(y, preferencesQualitative, x)

# print()
# print("Preference : Penalty Logic")
# print(t)
# print()
# print("Preference : Possibility Logic")
# print(k)
# print()
# print("Preference : Qualitative Logic")
# print(n)


print()
print("Preference : Penalty Logic")
for i in t:
    print(i)
print()
print("Preference : Possibility Logic")
for i in k:
    print(i)
print()
print("Preference : Qualitative Logic")
for i in n:
    print(i)


# exemplification
# s=random.sample(models, 2)
#
# print(s)