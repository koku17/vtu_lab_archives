print("\
	\nMissionaries & cannibals \
	\nNow the task is to move all of them to right side of the river \
	\n\
	\nRules : \
	\n1. The boat can carry at most two people \
	\n2. If cannibals number greater than missionaries then the cannibals would eat the \
	\n   missionaries \
	\n3. The boat cannot cross the river by itself with no people on board")

lM = 3    #lM = Left side Missionaries number
lC = 3    #lC = Left side Cannibals number
rM = 0    #rM = Right side Missionaries number
rC = 0    #rC = Right side cannibals' number
userM = 0 #userM = User input for number of missionaries for right to left side travel
userC = 0 #userC = User input for number of cannibals for right to left travel
k = 0

# Initial Position
print("\nM M M C C C | --- |")

# Get Current Position
def POS():
	print("")
	for i in range(0,lM):
		print("M ",end="")
	for i in range(0,lC):
		print("C ",end="")
	print("| --> | ",end="")
	for i in range(0,rM):
		print("M ",end="")
	for i in range(0,rC):
		print("C ",end="")
	print("")
	return None

# Get user input and return for missionaries and cannibals
def IN():
	M = int(input("Enter number of Missionaries travel => "))
	C = int(input("Enter number of Cannibals travel => "))
	return M,C

try:
	while(True):
		while(True):
			print("\nLeft side -> right side river travel\n")
			uM,uC=IN()
			if((uM==0)and(uC==0)):
				print("Empty travel not possible\nRe-enter : ")
			elif(((uM+uC) <= 2) and ((lM-uM) >= 0) and ((lC-uC) >= 0)):
				break
			else:
				print("\nWrong input re-enter !")
		lM -= uM
		lC -= uC
		rM += uM
		rC += uC
		POS()
		k += 1
		if(lC>lM or rC>rM):
			print("\nCannibals ate missionaries !\nYou lost the game :(\n")
			break
		if((rM+rC) == 6):
			print("\nYou won the game Congrats !\nTotal attempt(s) : ",k)
			break
		while(True):
			print("\nRight side -> Left side river travel\n")
			userM,userC=IN()
			if((userM==0)and(userC==0)):
				print("Empty travel not possible\nRe-enter : ")
			elif(((userM+userC) <= 2) and ((rM-userM)>=0) and ((rC-userC)>=0)):
				break
			else:
				print("\nWrong input re-enter !")
			lM += userM
			lC += userC
			rM -= userM
			rC -= userC
			POS()
			k += 1
			if(lC>lM or rC>rM):
				print("\nCannibals ate missionaries !\nYou have lost the game :(\n")
				break
except EOFError as e:
	print("\nInvalid input please retry !!")
