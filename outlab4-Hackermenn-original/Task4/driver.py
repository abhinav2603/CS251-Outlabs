import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from task4 import mean_filter,generate_sin_wave,noisify

def driver():
	clean_sin=generate_sin_wave(2,(-2,8),1000)
	dirty_sin=noisify(clean_sin,0.0025)
	cleaned_sin=mean_filter(dirty_sin,1)
	x=np.linspace(-2, 8, 1000)

	plt1=plt.plot(x,clean_sin)
	plt.title('Clean Sine wave')
	plt.savefig('clean_sin.png')
	plt.clf()

	plt2=plt.plot(x,dirty_sin)
	plt.title('Dirty Sine wave')
	plt.savefig('dirty_sin.png')
	plt.clf()

	plt3=plt.plot(x,cleaned_sin)
	plt.title('Cleaned Sine wave')
	plt.savefig('cleaned_sin.png')
	plt.clf()
driver()
