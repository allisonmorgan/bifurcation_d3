import matplotlib.pyplot as plt
import numpy as np

"""
Write a program that displays $m$ iterates of the logistic equation on the axes $x_{n}$ versus $R$ (a ``bifurcation plot''), but add an argument l that allows the user to suppress the plotting of the first l points (the transient). Turn in a bifurcation plot for the range $2.8 < R < 4$. Pick $l$, $m$, and the interval between $R$ values such that the details of the behavior are visible, but not such that the plot requires exorbitant amounts of CPU time.
"""

# Given the previous step, return the current step
def logistic_map(xn, R):
	return R*xn*(1.0 - xn)

# Specify initial conditions and iterate ...
def iterate_logistic_map(x0, R, m, l):
	ns = range(m); xns = []
	for n in ns:
		if n == 0:
			xn = x0
		else:
			xn = logistic_map(xn, R)

		xns.append(xn)

	return xns[l:]

r_vs_xn = {}; x0 = 0.2; m = 200; l = 100
for r in np.linspace(0.0, 4.0, 5000):
	steady_state = iterate_logistic_map(x0, r, m, l)
	r_vs_xn[r] = steady_state

# Convert this dictionary to a list of x's and y's
xs = []; ys = [];
for r in sorted(r_vs_xn.keys()):
	for xn in r_vs_xn[r]:
		xs.append(r)
		ys.append(xn)

#plt.scatter(xs, ys, color='blue', s=0.01)
#plt.ylim(0, 1.0)
#plt.xlim(0.0, 4.0)
#plt.ylabel(r'$x_{n}$', fontsize=20)
#plt.xlabel(r'$R$', fontsize=20)
#plt.savefig("bifurcations_full.png")
#plt.clf()

"""
Repeat problem $2$ with the Henon map:
$$
x_{k+1} = y_{k} + 1 - ax_{k}^{2},
y_{k+1} = bx_{k}
$$
Use $b = 0.3$ and $0 < a < 1.4$ \dots Please also turn in a plot of the bifurcation diagram of this map.
"""

# Given the previous step, return the current step
def henon_map(xn, yn, a, b):
	return ((yn + 1 - a*(xn**2)), b*xn)

# Specify initial conditions and iterate ...
def iterate_henon_map(x0, y0, a, b, m, l):
	ns = range(m); xns = []; yns = [];
	for n in ns:
		if n == 0:
			xn = x0
			yn = y0
		else:
			(xn, yn) = henon_map(xn, yn, a, b)

		xns.append(xn)
		yns.append(yn)

	return (xns[l:], yns[l:])

a_vs_xn = {}; a_vs_yn = {}; x0 = 0.1; y0 = 0.0; b = 0.3; m = 200; l = 100
for a in np.linspace(0.0, 1.4, 4000):
	steady_state = iterate_henon_map(x0, y0, a, b, m, l)
	a_vs_xn[a] = steady_state[0]
	a_vs_yn[a] = steady_state[1]

# Convert this dictionary to a list of x's and y's
xs = []; ys = [];
for a in sorted(a_vs_xn.keys()):
	for xn in a_vs_xn[a]:
		xs.append(a)
		ys.append(xn)

#plt.scatter(xs, ys, color='blue', s=0.01)
#plt.ylim(-1.5, 1.5)
#plt.xlim(0.0, 1.4)
#plt.ylabel(r'$x_{n}$', fontsize=20)
#plt.xlabel(r'$a$', fontsize=20)
#plt.savefig("bifurcations_henon_full.png")
#plt.clf()



