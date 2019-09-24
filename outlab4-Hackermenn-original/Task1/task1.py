# import here
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.misc import derivative
num=1000
def fn_plot1d(fn, x_min, x_max, filename):
    x=np.linspace(x_min,x_max,num)
    f=np.vectorize(fn)
    plt.plot(x,f(x))
    plt.savefig(filename)
    plt.clf()

def h(x):
    if x > 0:
    	return np.exp(-1/(x**2))
    else:
    	return 0

def g(x):
    return h(2-x) / (h(2-x)+h(x-1))

def b(x):
    return g(np.abs(x))

fn_plot1d(b,-2,2,'fn1plot.png')

def fn_plot2d(fn, x_min, x_max, y_min, y_max, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    f=np.vectorize(fn)
    x=np.linspace(x_min,x_max,num)
    y=np.linspace(y_min,y_max,num)
    X,Y=np.meshgrid(x,y)
    zs=np.array(f(np.ravel(X),np.ravel(Y)))
    Z=zs.reshape(X.shape)
    ax.plot_surface(X,Y,Z)
    plt.savefig(filename)
    plt.clf()
    #pass

def twodsinc(x,y):
    a=np.sqrt(x**2 + y**2)
    if a > 0:
    	return np.sin(a)/a
    else:
    	return 1
    #pass

fn_plot2d(twodsinc,-1.5*np.pi,1.5*np.pi,-1.5*np.pi,1.5*np.pi,'fn2plot.png')

def func(x):
	return x**2

def nth_derivative_plotter(fn, n, x_min, x_max, filename):
    x=np.linspace(x_min,x_max,num)
    f=np.vectorize(fn)
    if n%2 == 0:
    	z=n+5
    else:
    	z=n+4
    plt.plot(x,derivative(f,x,dx=1e-2,n=n,order=z))
    plt.savefig(filename)
    plt.clf()

def func(x):
	return x**2

for i in range(10):
	j=i+1
	file='bd_'+str(j)+'.png'
	nth_derivative_plotter(b,j,-2,2,file)



