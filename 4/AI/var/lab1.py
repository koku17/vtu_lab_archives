
# Set up jugs
j1=[4,0]
j2=[3,0]

def fill(jug):
	return jug[0]

def pour(j1,j2):
	if j2[1]<j2[0]:
		if j1[1]>j2[0]-j2[1]:
			return j1[1]-(j2[0]-j2[1]),j2[0]
		else:
			return 0,j1[1]+j2[1]
	return j1[1],j2[1]

j1[1]=fill(j1)
j1[1],j2[1]=pour(j1,j2)
j1[1]=fill(j1)
j1[1],j2[1]=pour(j1,j2)

j2[1]=fill(j2)
j2[1],j1[1]=pour(j2,j1)
j2[1]=fill(j2)
j2[1],j1[1]=pour(j2,j1)
