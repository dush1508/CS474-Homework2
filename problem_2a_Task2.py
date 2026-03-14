from z3 import *

# Declaring variables
l1, l2, u1, u2, z, w = Reals('l1 l2 u1 u2 z w')

# Original formula 
phi = ForAll([z],
    Implies(
        And(l1 < z, z < u1, l2 < z, z < u2),
        Exists([w],
            And(l1 < w, w < u1, l2 < w, w < u2, w != z)
        )
    )
)

# Performing quantifier elimination
qe_result = Tactic('qe')(phi)
print(qe_result)

# My answer
psi = True

prove(psi == qe_result.as_expr())