from sympy import symbols, pi
from dh    import DH


dh_chain = DH()
a1, theta1 = symbols('a1 theta1')
a2, theta2 = symbols('a2 theta2')

# link(d, theta, a, alpha)
dh_chain.link(0, theta1, a1, 0)
dh_chain.link(0, theta2, a2, 0)

print('TWO LINK PLANAR TEST')
print('--------------------')
dh_chain.summary()

