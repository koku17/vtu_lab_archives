op=[1,7,5,8,2,4,6,3]

r=[[0 for i in range(0,8)] for j in range(0,8)]

j=0
for i in range(0,8):
	r[op[i]-1][j]=1
	j+=1
print(r)
