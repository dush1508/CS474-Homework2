from z3 import *

# interval endpoints
l1,u1 = Reals('l1 u1')
l2,u2 = Reals('l2 u2')
l3,u3 = Reals('l3 u3')
l4,u4 = Reals('l4 u4')

s = Solver()

# valid intervals
s.add(l1 < u1)
s.add(l2 < u2)
s.add(l3 < u3)
s.add(l4 < u4)

def intersect(lA,uA,lB,uB):
    return And(lA < uB, lB < uA)

def no_intersect(lA,uA,lB,uB):
    return Or(Not(lB < uA), Not(lA < uB))

# Edge Constraints
s.add(intersect(l1,u1,l2,u2))
s.add(intersect(l2,u2,l3,u3))
s.add(intersect(l3,u3,l4,u4))
s.add(intersect(l1,u1,l4,u4))

# Non-Edge Constraints
s.add(no_intersect(l1,u1,l3,u3))
s.add(no_intersect(l2,u2,l4,u4))


print(s.check())