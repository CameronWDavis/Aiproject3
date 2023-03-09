from pysat.solvers import Glucose3
from pysat.formula import CNF
from input import *
from pysatSolve import *
import math


# iterate over the preferences and calculate their penalties


def preferencePenalty(model, preference_penalty):
    total_penalty = 0

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
        print(f"Penalty for model '{model}' and preference '{preference}': {preference_penalty_value}")

    # print the total penalty for the model
    print(f"Total penalty for the model '{model}': {total_penalty}")
    print()


def preferencePossibility(model, preference_possibility):
    total_tolerance = 0
    values = []

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
        print(f"Tolerance for model '{model}' and preference '{preference}': {preference_penalty_value}")

    # print the total penalty for the model
    print(f"Total tolerance for the model '{model}': {total_tolerance}")
    print()


def preferenceQualitative(model, preference_qualitative, modelV):
    satisfaction = math.inf
    for items in preference_qualitative:
        for preference in items["preference"]:
            conditionNow = items["condition"]
            if not solve(model, transform(conditionNow)):
                break

                if solve(model, transform(preference)):
                    satisfaction = items["preference"].index(preference) + 1

            print(
                f"Satisfaction for model '{modelV}' and preference '{preference}' and condition {conditionNow}: {satisfaction}")

    print(
        f"Satisfaction for model '{modelV}' and preference '{preference}' and condition {conditionNow}: {satisfaction}")


def transform(model):
    clauses = []
    # read each line in the file
    for pref in model:
        # remove the newline character
        pref = pref.strip()
        # split the line by 'OR'
        tokens = pref.split('OR')
        # initialize an empty list to store the literals
        literals = []
        # iterate over the tokens
        for token in tokens:
            # remove whitespace
            token = token.strip()
            # check if the token starts with 'NOT'
            if token.startswith('NOT'):
                # get the literal name (without the 'NOT' prefix)
                literal = token[4:]
                # look up the integer value of the literal in the dictionary
                value = -original_dict[literal]
            else:
                # look up the integer value of the literal in the dictionary
                value = original_dict[token]
            # add the literal to the list
            literals.append(value)
        # add the clause to the list of clauses
        clauses.append(literals)
        return clauses


print()
print("Prefernce : Penalty Logic")
for model in models:
    preferencePenalty(model, preferencesPenalty)
print()
print("Prefernce : Possibility Logic")
for model in models:
    preferencePossibility(model, preferencesPossibility)
print()
print("Prefernce : Qualitative Logic")
for x, y in zip(models, modelsCNF):
    # print()
    preferenceQualitative(y, preferencesQualitative, x)
