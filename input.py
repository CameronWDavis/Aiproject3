# this is used to read the attribute file and stored everything in a menu dict
with open('ExampleCase/myAttirbute.txt', 'r') as file:
    contents = file.read()

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

# print(original_dict)


# this is used to read the constraints file and add everything to the clauses list
with open('ExampleCase/myConstraints.txt', 'r') as f:
    # initialize an empty list to store the clauses
    clauses = []
    # read each line in the file
    for line in f:
        # remove the newline character
        line = line.strip()
        # split the line by 'OR'
        tokens = line.split('OR')
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

# print(clauses)

# for penalty logic
preferencesPenalty = {}

# Open the file and read each line
with open('ExampleCase/myPenaltyLogic.txt', 'r') as f:
    for line in f:
        # Split the line into the preference and the penalty
        items = line.strip().split(', ')
        if len(items) == 2:
            preference, penalty = items

            # Store the preference and the penalty in the dictionary
            preferencesPenalty[preference] = int(penalty)

    # for preference, penalty in preferencesPenalty.items():
    #     print(f"{preference} = {penalty}")
# print(preferencesPenalty)
print()
# for possibility logic
preferencesPossibility = {}

# Open the file and read each line
with open('ExampleCase/myPossibilisticLogic.txt', 'r') as f:
    for line in f:
        # Split the line into the preference and the penalty
        items = line.strip().split(', ')
        if len(items) == 2:
            preference, penalty = items

            # Store the preference and the penalty in the dictionary
            preferencesPossibility[preference] = float(penalty)
    # Print the preferences and penalties
    # for preference, penalty in preferencesPossibility.items():
    # print(f"{preference} = {penalty}")

# for qualitative logic:


preferencesQualitative = []
with open('ExampleCase/myQualititaveLogic.txt', 'r') as f:
    for line in f:
        preferences = line.strip().split('BT')
        preference_list = []
        for preference in preferences:
            if 'IF' in preference:
                preference_list.append([preference[:preference.find('IF')].strip()])
            else:
                preference_list.append([preference.strip()])
        c = line.split('IF')
        condition = c[1].strip()
        preferencesQualitative.append({'preference': preference_list, 'condition': [condition], 'statement': line.rstrip()})

# print(preferencesQualitative)

def assign_binary(lst):
    binary_digits = [1 if val >= 0 else 0 for val in lst]
    binary_str = ''.join(str(digit) for digit in binary_digits)
    binary_value = int(binary_str, 2)
    return binary_value


def to_subscript(n):
    subscript_digits = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(n).translate(subscript_digits)
