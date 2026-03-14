from z3 import *

p, q, r = Bools('p q r')

phi = And(
    Or(q, Not(r)),
    Or(Not(p), r),
    Or(Not(q), r, p),
    Or(p, q, Not(q)),
    Or(Not(r), q)
)

psi = And(
    Or(q, Not(r)),
    Or(Not(p), r),
    Or(Not(q), r, p),
    Or(q, Not(p)),
    Or(Not(q), r)
)

s = Solver()

print("Checking satisfiability of phi")
s.push()
s.add(phi)
print(s.check())
s.pop()

s.push()
s.add(Not(phi == psi))
result = s.check()

if result == unsat:
    print("phi and psi are equivalent")
else:
    print("phi and psi are NOT equivalent")
    print("Counterexample:", s.model())