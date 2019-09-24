import numpy as np

def mean_filter(arr,k):
	temp=arr.copy()
	temp.astype(dtype='float')
	l=np.size(temp)
	helper=np.zeros(k)
	temp=np.append(temp,helper)
	cusum=np.cumsum(temp)
	helper2=np.zeros(2*k+1)
	cusums=np.append(helper2,cusum)
	cusume=np.append(cusum,helper2)
	cusum1=cusume-cusums
	cusum2=cusum1[k:l+k]
	cusum2=cusum2/(2*k+1)
	#print(cusum2.shape,arr.shape,cusum2)
	return cusum2

def generate_sin_wave(period,range_,num):
	pii=np.pi
	amin=range_[0]*2*pii/period
	amax=range_[1]*2*pii/period
	temp=np.linspace(amin,amax,num)
	temp=np.sin(temp)
	return temp

def noisify(array,var):
	temp=array.copy()
	x=temp.size
	sigma=np.sqrt(var)
	temp=temp+np.random.normal(0,sigma,x)
	return temp

#print(mean_filter(np.arange(6)+1,1))
