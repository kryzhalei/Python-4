import matplotlib.pyplot as plt
import numpy as np
import math

y = input('Enter Initial Height: ');
v = input('Enter Initial Velocity: ');
th = input('Enter Initial Angle: ');
ax = input('Enter Acceleration in X: ');
ay = input('Enter Acceleration in Y: ');

y = float(y)
v = float(v)
th= float(th)
ax = float(ax)
ay = float(ay)

if ay == 0:
    print('Vertical Acceleration Cannot be 0!')
else:
    q = ((2*v*math.sin(math.radians(th)))/(-1*ay)) + (y/(v*math.sin(math.radians(th))))
    t = np.arange(0,q,0.01)
    
    c = 0
    xp = np.array([])
    yp = np.array([])

    while (c<q):
        xm = (v*math.cos(math.radians(th)))*c + 0.5*(ax)*c**2;
        ym = y + (v*math.sin(math.radians(th)))*c + 0.5*(ay)*c**2;
    
        xp = np.append(xp,xm)
        yp = np.append(yp,ym)
    
        c = c + 0.01

    plt.plot(xp,yp)