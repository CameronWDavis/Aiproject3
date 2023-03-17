# the standard way to import PySAT:
from pysat.formula import CNF
from pysat.solvers import Solver
from input import *


# this how the mapping dictionary look we if we consider this example attributes
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

def getModelObject(model_tested):
    b = '0'f"{to_subscript(assign_binary(y))}"
    return b


new_dict = {v: k for k, v in original_dict.items()}

clauses.extend([[-x, x] for x in range(1, len(menu) + 1)])

cnf = CNF(from_clauses=clauses)

# create a constraint : not noodle or tomato : [4, -5]
# cnf = CNF(from_clauses=[[4, -5],[-1,1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7,7], [-8,8]])

# create a satisfiable CNF formula "(-x1 ∨ x2) ∧ (-x1 ∨ -x2)":
# cnf = CNF(from_clauses=[[-1, 2], [-1, -2]])

# create a SAT solver for this formula:
with Solver(bootstrap_with=cnf) as solver:
    # # 1.1 call the solver for this formula:
    # print('formula is', f'{"s" if solver.solve() else "uns"}atisfiable')

    # # 1.2 the formula is satisfiable and so has a model:
    # print('and the model is:', solver.get_model())

    # enumerate al models :

    print("Here are all the feasible objects models of this formula:")

    models = []
    modelsCNF = []
    for m in solver.enum_models():
        modelsCNF.append(m)
        model_dict = [new_dict[x] for x in m]
        models.append(model_dict)

    for x, y in zip(models, modelsCNF):
        # print('0'f"{to_subscript(assign_binary(y))}", x)
        print(getModelObject(y), x)
    # all the model of the formula satisfying are saved in models list


# this method solve the satisfiability
def solve(model, conditions):
    if conditions == 0:
        return True
    else:

        conditions.extend([[-x, x] for x in range(1, len(menu) + 1)])
        # print("the clauses is", conditions)
        cnf1 = CNF(from_clauses=conditions)
        # print(model)
        with Solver(bootstrap_with=cnf1) as solver1:
            #  call the solver for this formula:
            return solver1.solve(assumptions=model)
