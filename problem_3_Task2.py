from z3 import *

x = Real('x')
y = Real('y')

psi = ForAll(
    [x],
    Exists(
        [y],
        And(2*y > 3*x,
            4*y < 8*x + 10)
    )
)

s = Solver()
s.add(Not(psi))

print(s.check())