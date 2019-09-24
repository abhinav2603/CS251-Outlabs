import numpy as np 
from scipy.cluster.vq import kmeans2 
import matplotlib.pyplot as plt
import imageio as im
import sys
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--input",required=True)
parser.add_argument("--output",required=True)
parser.add_argument("--k",required=True)
args = parser.parse_args()

inpt=args.input
k=int(args.k)
output=args.output

a=im.imread(inpt)
a=np.array(a,'float')
M=np.copy(a)
M1=M[:,:,:3:1]
r=np.size(M,0)
c=np.size(M,1)
#print(M.shape)

M1.shape=(r*c,3)
centroid,label = kmeans2(M1,k,minit='++',iter=200)
#x=np.ones(r*c,'int'):
M1=centroid[label]
M1.shape=(r,c,3)
M1=np.array(M1,'uint8')
im.imwrite(output,M1)
