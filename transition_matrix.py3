import matplotlib.pyplot as plt
import numpy as np

switcher={57: 24, 78: 30, 53: 17, 72: 48, 5: 34, 25: 42, 9: 31, 36: 55}						#provides the positions of the snakes and ladders. 
		
trans_array=np.zeros(shape=(100,100))
i=0

for i in range(0,100):												#creates the basic transition matrix without snakes and ladders
	for j in range(1,7):
		if i<94:
			trans_array[i][i+j]=1/6
		if i>=94:
			rem=i-93
			trans_array[i][i]=rem/6
			if j<=99-i:
				trans_array[i][i+j]=1/6

i=0
n=0
for i in switcher.keys():											#adds the snakes and ladders to the matrix
	if i<switcher.get(i):
		for j in range(0,100):
			trans_array[j][i]=0
			if i-j<=6 and i-j>0:
				trans_array[j][switcher.get(i)]=1/6
					
	if i>switcher.get(i):
		for j in range(0,100):
			trans_array[j][i]=0
		for n in range(switcher.get(i),100):
			if n+6>=i and n<=i:	
				trans_array[n][switcher.get(i)]=1/6
	


i=0
for i in switcher.keys():											#makes the row containing snakes and ladders to be 1
	trans_array[i]=0
	trans_array[i][switcher.get(i)]=1


i=0
n=0
j=0
arr=list(switcher.keys())
arr.sort()
for i in arr:														#deletes the rows and columns containing the snakes and ladders
	trans_array=np.delete(trans_array,i-j,0)
	trans_array=np.delete(trans_array,i-j,1)
	j+=1

rows,columns=trans_array.shape

vector=np.zeros(shape=(1,rows))										#creates the initial vector with 1 in first position
vector[0][1] = 1

i=0
j=0	
prob = []

while True:															#multiplies the vector withe matrix itiratively
	i+=1
	newvector=vector.dot(trans_array)	
	vector=newvector
	sumv=np.sum(vector)
	prob.append(vector[0][91])
	if vector[0][91]>0.99:											#stops when the final element reaches a value of 0.99. This is just to break out of the loop.
		print(i)
		break

x=[k for k in range(0,len(prob))]

print(vector)
plt.plot(x,prob)
plt.show()




	





