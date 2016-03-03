import numpy as np
import matplotlib.pyplot as plt
import math

t = np.arange(-2, 2, 0.01)
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

def plot_circle(cx, cy, r, ax):
	ts = np.arange(0, math.pi*2, 0.01)
	xs = [cx+r*math.cos(t) for t in ts]
	ys = [cy+r*math.sin(t) for t in ts]
	ax.plot(xs, ys, color='red')

x = [real(ts) for ts in t]
y = [imaginary(ts) for ts in t]

r = [math.log(modular(x[index], y[index]), q) for index in xrange(1, len(t))]
i = [argument(x[index], y[index]) for index in xrange(1, len(t))]


fig = plt.figure()

ax = fig.add_subplot(212)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.set_title(r'$D_W$')
ax.axis([-2, 2, -4, 4])
ax.get_xaxis().set_ticklabels([])
ax.get_yaxis().set_ticklabels([])
ax.set_aspect('equal')

ax.plot(r,i,color='black', ls='dotted')

wx = r[290]
wy = i[290]
ax.plot(wx,wy,'o',color='black')
ax.annotate('W', xy=(wx,wy), xytext=(wx-0.1, wy+0.1))

ax.plot(wx+1,wy,'o', color='black')
ax.annotate('W+1', xy=(wx+1,wy), xytext=(wx+1-0.1, wy+0.1))

ax.plot(wx+2,wy,'o', color='black')
ax.annotate('W+2', xy=(wx+2,wy), xytext=(wx+2-0.1, wy+0.1))

plot_circle(wx+1, wy, 0.08, ax)
plot_circle(wx+2, wy, 0.08, ax)

R = 1.8
intersecty = 0.3247176601*math.sin(phi)

d1x = np.empty(100)
d1x.fill(R)
d1x = d1x.tolist()
d1y = [-6 + ns*0.12 for ns in xrange(0,100,1)]

ax.plot(d1x,d1y,color='red')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.set_title(r'$D_W$')
ax.axis([-2, 2, -1, 1])
ax.get_xaxis().set_ticklabels([])
ax.get_yaxis().set_ticklabels([])
ax.set_aspect('equal')

ax.plot(r,i,color='black', ls='dotted')

ax.annotate(r'$C_{\varphi}$',xy=(r[380], i[380]), xytext=(r[380], i[380]+0.1))

ax = fig.add_subplot(211)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.set_title(r'$D_W$')
ax.axis([-2, 2, -1, 1])
ax.get_xaxis().set_ticklabels([])
ax.get_yaxis().set_ticklabels([])
ax.set_aspect('equal')

ax.plot(r,i,color='black', ls='dotted')
ax.annotate(r'$C_{\varphi}$',xy=(r[380], i[380]), xytext=(r[380], i[380]+0.1))

ax.plot(wx,wy,'o',color='black')
ax.annotate('W', xy=(wx,wy), xytext=(wx-0.1, wy+0.1))

d = 0.07

d1x = np.empty(100)
d1x.fill(R)
d1x = d1x.tolist()
d1y = [wy-d-ns*0.02 for ns in xrange(0,100)]

d2x = [d1x[99]-(d1x[99]-0.5)*ns/100 for ns in xrange(0,100)]
d2y = np.empty(100)
d2y.fill(d1y[0])
d2y = d2y.tolist()

d3x = np.empty(100)
d3x.fill(0.5)
d3x = d3x.tolist()
d3y = [d2y[0]+(2*d)*ns/100 for ns in xrange(0,100)]

d4x = [d1x[99]-(d1x[99]-0.5)*ns/100 for ns in xrange(0,100)]
d4y = np.empty(100)
d4y.fill(d1y[0]+2*d)
d4y = d4y.tolist()

d5x = np.empty(100)
d5x.fill(R)
d5x = d5x.tolist()
d5y = [wy+d+ns*0.02 for ns in xrange(0,100)]

dx = d1x + d2x + d3x + d4x + d5x
dy = d1y + d2y + d3y + d4y + d5y
ax.plot(dx, dy,color='red')

plt.show()