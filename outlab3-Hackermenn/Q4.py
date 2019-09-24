import operator
lis=[]
x = int(input())
mydict={}
mydict3={}
i=0
while (i<x) :
	mydict2={}
	inp = [line for line in input().split()]
	for l in inp:
		temp = [a for a in l.split(":")]
		key=str(temp[0])
		temp1 = [b for b in temp[1].split(",")]
		mydict2={}
		for b in temp1 :
			temp2 = [c for c in b.split("-")]	
			mydict2[str(temp2[0])]=int(temp2[1])
			if str(temp2[0]) in mydict3:
				mydict3[str(temp2[0])]+=int(temp2[1])
			else:
				mydict3[str(temp2[0])]=int(temp2[1])
		mydict[key]=mydict2
	i+=1
for i in mydict3:
	lis.append((i,mydict3[i]))
print(mydict)
lis.sort(key = operator.itemgetter(1, 0), reverse=True)
print(lis)