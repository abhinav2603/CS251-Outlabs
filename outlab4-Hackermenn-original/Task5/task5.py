import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys


parser=argparse.ArgumentParser(description='Plot from csv')
parser.add_argument('--data',required=True,help='the path of data file')

ip=pd.read_csv(vars(parser.parse_args(sys.argv[1:]))['data'])
instance_grouped=ip.groupby('instance')

instance_no=3
for instance,group in instance_grouped:
	fig=plt.figure()
	algo_grouping=group.groupby(['algorithm'])
	for algo,algo_group in algo_grouping:
		if(algo=='epsilon-greedy'):
			eg_groups=algo_group.groupby('epsilon')
			for epsilon,eg_group in eg_groups:
				avg_eg_group=eg_group.groupby('horizon',as_index=False).agg({'REG':np.mean})#.reset_index(name='horizon')
				#print(avg_eg_group)
				#print(avg_eg_group['REG'].tolist())
				#avg_eg_group.plot()
				plt.plot(avg_eg_group['horizon'].tolist(),avg_eg_group['REG'].tolist(),label='epsilon-greedy with epsilon=' + str(epsilon))
				#break
		else:
			#pass
			avg_algo_group=algo_group.groupby('horizon',as_index=False).agg({'REG':np.mean})
			plt.plot(avg_algo_group['horizon'].tolist(),avg_algo_group['REG'].tolist(),label=algo)
			#print(algo_group['horizon'].tolist())
	plt.legend(loc='upper left')
	plt.xlabel('horizon')
	plt.ylabel('Regret')
	plt.title('Instance '+str(instance_no)+' - both axes in log scale')
	plt.yscale('log')
	plt.xscale('log')
	fig.savefig('instance'+str(instance_no))
	instance_no-=1
	#plt.show()