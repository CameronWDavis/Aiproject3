# this is used to read the attribute file and stored everything in a menu dictionary
from gui import *

print(field_contents)
# with open(field_contents['file1'], 'r') as file:
contents = field_contents['file1']

menu = {}
for line in contents.split('\n'):
    if ':' in line:
        category, items = line.split(':')
        menu[category.strip()] = [item.strip() for item in items.split(',')]

# original_dict = {
#     'soup': 1,
#     'chicken': 2,
#     'vegetable': 3,
#     'brocoli': 3,
#     'noodles': 4,
#     'teriyaki': 5,
#     'beer': 6,
#     'vanilla': 7,
#     'cake': 8,
#     'salad': -1,
#     'steak': -2,
#     'cabbage': -3,
#     'rice': -4,
#     'tomato': -5,
#     'wine': -6,
#     'chocolate': -7,
#     'ice-cream': -8
# }

# print(menu)

#####3
# assigning each item with a number and storing it in dict
original_dict = {}
for i, (key, value) in enumerate(menu.items()):
    # print(menu.items())
    for item in value:
        # print(value, "values")
        original_dict[item] = (i + 1) if item == value[0] else -(i + 1)

print(original_dict)

# this is used to read the constraints file and add everything to the clauses list
# with open(field_contents['file2'], 'r') as f:
f = field_contents['file2']
clauses = []
for line in f.split('\n'):
    print("line:", line)
    # remove the newline character
    line = line.strip()
    if line:
        tokens = line.split('OR')
        literals = []
        # iterate over the tokens
        for token in tokens:
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
                print(value)
            # add the literal to the list
            literals.append(value)
        # add the clause to the list of clauses
        clauses.append(literals)

# print(clauses)

# for penalty logic
preferencesPenalty = {}

# Open the file and read each line
# with open(field_contents['file3'], 'r') as f:

f = field_contents['file3']
# with open('myPenaltyLogic.txt', 'r') as f:
for line in f.split('\n'):
    if line.strip():  # check if the line is not empty
        # Split the line into the preference and the penalty
        items = line.strip().split(', ')
        if len(items) == 2:
            preference, penalty = items
            # Store the preference and the penalty in the dictionary
            preferencesPenalty[preference] = int(penalty)

print(preferencesPenalty, "penalty")
# for possibility logic
preferencesPossibility = {}

# Open the file and read each line
# with open(field_contents['file4'], 'r') as f:
f = field_contents['file4']
for line in f.split('\n'):
    if line.strip():
        # Split the line into the preference and the penalty
        items = line.strip().split(', ')
        if len(items) == 2:
            preference, penalty = items

            # Store the preference and the penalty in the dictionary
            preferencesPossibility[preference] = float(penalty)

print(preferencesPossibility)
# for qualitative logic:

preferencesQualitative = []
# with open(field_contents['file5'], 'r') as f:
f = field_contents['file5']
for line in f.split('\n'):
    print("line preference:", line)
    if line.strip():
        preferences = line.strip().split('BT')
        preference_list = []
        for preference in preferences:
            if 'IF' in preference:
                preference_list.append([preference[:preference.find('IF')].strip()])
            else:
                preference_list.append([preference.strip()])
        c = line.split('IF')
        condition = c[1].strip()
        preferencesQualitative.append(

            {'preference': preference_list, 'condition': [condition], 'statement': line.rstrip()})

print(preferencesQualitative)


def assign_binary(lst):
    binary_digits = [1 if val >= 0 else 0 for val in lst]
    binary_str = ''.join(str(digit) for digit in binary_digits)
    binary_value = int(binary_str, 2)
    return binary_value


def to_subscript(n):
    subscript_digits = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(n).translate(subscript_digits)
