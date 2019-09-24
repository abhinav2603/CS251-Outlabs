import re
import sys
file=open(sys.argv[1],'r')
content=file.read()
#lst=re.findall(r'\b[a-zA-Z0-9][a-zA-Z0-9._]+[a-zA-Z0-9]+@[a-zA-Z0-9.]+\.[a-zA-Z]+\b|[a-zA-Z0-9][a-zA-Z0-9._]+[a-zA-Z0-9]+@[a-zA-Z]+\b|\b[1-9][0-9]{9}\b',content)
lst=re.findall(r'(?!.*[\._@][_\.@].*)\b[a-zA-Z0-9]+[a-zA-Z0-9._]*[a-zA-Z0-9]*@[a-zA-Z0-9.]+\.[a-zA-Z]+\b|(?!.*[\._@][_\.@].*)\b[a-zA-Z0-9]+[a-zA-Z0-9._]*[a-zA-Z0-9]*@[a-zA-Z]+\b|\b[1-9][0-9]{9}\b',content)
mynum=sys.argv[2]
#print(lst)
d={}
for i in lst:
	if not(i in d):
		d[i]=1
	else:
		d[i]=d[i]+1

if not(mynum in d):
	d[mynum]=0

d2={}
state=True
for i in list(d):
	if not(i == mynum):
		if d[i] > d[mynum]:
			state=False
			if not(i in d2):
				d2[i]=d[i]
if state:
	print("my frequency:",d[mynum])
	print("It's all good yo!")
else:
	print("my frequency:",d[mynum])
	for i in list(d2):
		print("Cheater alert!",i,d2[i])

