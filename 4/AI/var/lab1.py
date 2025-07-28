# Set up jugs
j1=[4,0]
j2=[3,0]
steps=[]

def fill(jug):
	return jug[0]

def pour(j,k):
	if k[1]<k[0]:
		if j[1]>k[0]-k[1]:
			return j[1]-(k[0]-k[1]),k[0]
		else:
			return 0,j[1]+k[1]
	return j[1],k[1]

def check():
	if j1[1] == 2 or j2[1] == 2:
		if j1[1] == 2:
			j2[1]=0
		else:
			j1[1]=j2[1]
			j2[0]=0
		return True
	return False

def steps(j1,j2):
	i=1
	while i>0:
		if j1[0] > j2[0]:
			if (j2[0]*i) - j1[0] == 2:
				break
			elif (j1[0]*i) - j2[0] == 2:
				break
		i += 1
	return i

for i in range(0,steps(j1,j2)):
	steps[i]="Fill jug 2 !"
	j2[1]=fill(j2)
	steps[i+1]="Pour jug 2 to jug 1"
	j2[1],j1[1]=pour(j2,j1)
	if(check):
		print(steps)
		break

for i in range(0,steps(j1,j2)):
	steps[i]="Fill jug 1 !"
	j1[1]=fill(j1)
	steps[i+1]="Pour jug 1 to jug 2"
	j1[1],j2[1]=pour(j1,j2)
	if(check):
		print(steps)
		break
