import numpy as np
import matplotlib.pyplot as plt
from gekko import GEKKO

m = GEKKO()

# integration time points
m.time = np.linspace(0,10)

# constants
c1 = 0.13
c2 = 0.20
Ac = 2       # m^2
# inflow
qin1 = 0.5   # m^3/hr

# variables
h1 = m.Var(value=0,lb=0,ub=1)
h2 = m.Var(value=0,lb=0,ub=1)
overflow1 = m.Var(value=0,lb=0)
overflow2 = m.Var(value=0,lb=0)

# outflow equations
qin2 = m.Intermediate(c1 * h1**0.5)
qout1 = m.Intermediate(qin2 + overflow1)
qout2 = m.Intermediate(c2 * h2**0.5 + overflow2)

# mass balance equations
m.Equation(Ac*h1.dt()==qin1-qout1)
m.Equation(Ac*h2.dt()==qin2-qout2)

# minimize overflow
m.Obj(overflow1+overflow2)

# set options
m.options.IMODE = 6 # dynamic optimization

# simulate differential equations
m.solve()

# plot results
plt.figure(1)
plt.plot(m.time,h1,'b-')
plt.plot(m.time,h2,'r--')
plt.xlabel('Time (hrs)')
plt.ylabel('Height (m)')
plt.legend(['height 1','height 2'])
plt.show()