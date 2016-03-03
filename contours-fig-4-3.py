import numpy as np
import matplotlib.pyplot as plt
import math

t = np.arange(-0.2, 0.2, 0.001)
q = 0.5
theta =1.5
phi = math.pi * 55 / 128

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

r = [math.log(modular(x[index], y[index]), q) for index in xrange(1, len(t))]
i = [argument(x[index], y[index]) for index in xrange(1, len(t))]


fig = plt.figure()

ax = fig.add_subplot(111)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.set_title(r'$C_{\varphi}$')
ax.axis([1, 2, -1, 1])
ax.get_xaxis().set_ticklabels([])
ax.get_yaxis().set_ticklabels([])
ax.set_aspect('equal')
ax.plot(r,i,color='black')

ax.annotate(r'$C_{\varphi}$', xy=(r[380], i[380]))

R = 1.67
r = 0.3247176601
# intersecty = 0.3247176601*math.sin(phi)

# d1x = np.empty(100)
# d1x.fill(R)
# d1x = d1x.tolist()
# d1y = [-intersecty - ns*0.03 for ns in xrange(100,0,-1)]

# d2x = [1.5+ts*math.cos(-phi) for ts in np.arange(0.3247176601,0,-0.003247176601)]
# d2y = [ts*math.sin(-phi) for ts in np.arange(0.3247176601,0,-0.003247176601)]

# d3x = [1.5+ts*math.cos(phi) for ts in np.arange(0, 0.3247176601,0.003247176601)]
# d3y = [ts*math.sin(phi) for ts in np.arange(0, 0.3247176601,0.003247176601)]

# d4x = np.empty(100)
# d4x.fill(R)
# d4x = d4x.tolist()
# d4y = [intersecty+ns*0.03 for ns in xrange(0,100,1)]

# dx = d1x + d2x + d3x + d4x
# dy = d1y + d2y + d3y + d4y

circlex = [1.5+r*math.cos(angle) for angle in np.arange(0,2*math.pi,0.01)]
circley = [r*math.sin(angle) for angle in np.arange(0,2*math.pi,0.01)]

ax.plot(circlex, circley, ls='dotted')

intersecty = 0.28

d1x = np.empty(100)
d1x.fill(R)
d1x = d1x.tolist()
d1y = [-1 + (1-intersecty)*ns/100 for ns in xrange(0,100) ]

d2x = [1.67-0.17*ns/100 for ns in xrange(0,100)]
d2y = [intersecty*1.5/0.17 - intersecty*xs/0.17 for xs in d2x]

d3x = d2x[::-1]
d3y = [-d2ys for d2ys in d2y[::-1]]

d4x = d1x
d4y = [intersecty+(1-intersecty)*ns/100 for ns in xrange(0,100)]

ax.annotate(r'$D_{W}$', xy=(d4x[20], d4y[20]))

dx = d1x + d2x + d3x + d4x
dy = d1y + d2y + d3y + d4y

ax.plot(dx,dy,color='black')

dd1x = [1.34+0.16*ns/100 for ns in xrange(0,100)]
dd1y = [intersecty - ns*intersecty/100 for ns in xrange(0,100)]

dd2x = dd1x[::-1]
dd2y = [-d2yy for d2yy in dd1y[::-1]]

ddx = dd1x + dd2x
ddy = dd1y + dd2y

ax.plot(ddx, ddy,color='black')

ax.annotate(r'$\theta$', xy=(theta,0), xytext=(theta, 0.08))

plt.show()