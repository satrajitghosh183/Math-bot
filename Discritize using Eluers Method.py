import numpy as np
import matplotlib.pyplot as plt

def tank(c1,c2):
  Ac = 2 # m^2
  qin = 0.5 # m^3/hr
  dt = 0.5 # hr
  tf = 10.0 # hr

  h1 = 0
  h2 = 0
  t = 0
  ts = np.empty(21)
  h1s = np.empty(21)
  h2s = np.empty(21)
  i = 0
  while t<=10.0:
     ts[i] = t
     h1s[i] = h1
     h2s[i] = h2

     qout1 = c1 * pow(h1,0.5)
     qout2 = c2 * pow(h2,0.5)
     h1 = (qin-qout1)*dt/Ac + h1
     if h1>1:
        h1 = 1
     h2 = (qout1-qout2)*dt/Ac + h2
     i = i + 1
     t = t + dt

  # plot data
  plt.figure(1)
  plt.plot(ts,h1s)
  plt.plot(ts,h2s)
  plt.xlabel("Time (hrs)")
  plt.ylabel("Height (m)")
  plt.show()

# call function
tank(0.13,0.20)