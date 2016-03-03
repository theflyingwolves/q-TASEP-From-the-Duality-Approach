import numpy as np
import matplotlib.pyplot as plt
import math

# evenly sampled time at 200ms intervals
t = np.arange(-2, 2, 0.1)
q = 0.5
theta =1.5
phi = math.pi / 8

def sign(x):
	if x >= 0:
		return 1
	else:
		return -1

def real(t):
	return math.pow(q, theta)+math.fabs(t)*math.cos(phi*sign(t))

def imaginary(t):
	return math.fabs(t)*math.sin(phi*sign(t))

def modular(r, i):
	return math.hypot(r,i)

def argument(r,i):
	return math.atan2(i,r)

x = [real(ts) for ts in t]
y = [imaginary(ts) for ts in t]

fig = plt.figure()

ax = fig.add_subplot(1, 3, 1)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.set_title(r'$\tilde{C}_{\varphi}$')
# ax.axis([-2, 3, -1, 1])
ax.plot(x,y,color='black')

r = [math.log(modular(x[index], y[index]), q) for index in xrange(1, len(t))]
i = [argument(x[index], y[index]) for index in xrange(1, len(t))]

ax = fig.add_subplot(1,3,2)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.set_title(r'$C_{\varphi}$')
ax.axis([-1.5, 2, -0.4, 0.4])
ax.plot(r,i,color='black')

R = 5
d = 0.5

d1x = np.empty(100)
d1x.fill(R)
d1y = [-d-ns*0.03 for ns in xrange(100,0,-1)]

d2x = [0.5+ts*0.015 for ts in xrange(100,0,-1)]
d2y = np.empty(100)
d2y.fill(-d)

d3x = np.empty(100)
d3x.fill(0.5)
d3y = [-d+ns*0.01 for ns in xrange(0,100)]

d4x = [0.5+ns*0.015 for ns in xrange(0,100)]
d4y = np.empty(100)
d4y.fill(d)

d5x = np.empty(100)
d5x.fill(R)
d5y = [d + ns * 0.03 for ns in xrange(0,100)]

dx = np.empty(500)
dy = np.empty(500)

for ind in xrange(0,100):
	dx[ind] = d1x[ind]
	dy[ind] = d1y[ind]

for ind in xrange(100,200):
	dx[ind] = d2x[ind-100]
	dy[ind] = d2y[ind-100]

for ind in xrange(200,300):
	dx[ind] = d3x[ind-200]
	dy[ind] = d3y[ind-200]

for ind in xrange(300,400):
	dx[ind] = d4x[ind-300]
	dy[ind] = d4y[ind-300]

for ind in xrange(400,500):
	dx[ind] = d5x[ind-400]
	dy[ind] = d5y[ind-400]

ax = fig.add_subplot(1,3,3)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.set_title(r'${\tilde{D}_{w}}$')
ax.plot(dx, dy,color='black')
ax.axis([0,R+0.5,-3,3])

plt.show()