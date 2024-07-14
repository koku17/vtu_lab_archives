#!/bin/python

print(
	'\n\tGame Start \
	\nNow the task is to move all of them to right side of the river \
	\nRules : \
	\n1. The boat can carry at most two people \
	\n2. If cannibals number greater than missionaries then the cannibals would eat the missionaries \
	\n3. The boat cannot cross the river by itself with no people on board'
)

lM=3    #lM=Left side Missionaries number
lC=3    #lC=Laft side Cannibals number
rM=0    #rM=Right side Missionaries number
rC=0    #rC=Right side cannibals’ number
userM=0 #userM=User input for number of missionaries for right to left side travel
userC=0 #userC=User input for number of cannibals for right to left travel
k=0

print('\nM M M C C C | --- | \n')
try:
	while(True):
		while(True):
			print('Left side-> right side river travel')
			uM=int(input('Enter number of Missionaries travel=> '))
			uC=int(input('Enter number of Cannibals travel=> '))
			if uM==0 and uC==0:
				print('Empty travel not possible\nRe-enter : ')
			elif (uM+uC)<=2 and (lM-uM)>=0 and (lC-uC)>=0:
				break
			else:
				print('Wrong input re-enter : ')
		lM=(lM-uM)
		lC=(lC-uC)
		rM+=uM
		rC+=uC
		print('')
		for i in range(0,lM):
			print('M ',end='')
		for i in range(0,lC):
			print('C ',end='')
		print('| --> | ')
		for i in range(0,rM):
			print('M ',end='')
		for i in range(0,rC):
			print('C ',end='')
		print('')
		k+=1
		if (lC==3 and lM==1) or (lC==3 and lM==2) or (lC==2 and lM==1) or (rC==3 and rM==1) or \
			(rC==3 and rM==2) or (rC==2 and rM==1):
			print('Cannibals eat missionaries:\nYou lost the game')
			break
		if rM+rC==6:
			print('You won the game : \n\tCongrats')
			print('Total attempt')
			print(k)
			break
		while(True):
			print('Right side-> Left side river travel')
			userM=int(input('Enter number of Missionaries travel=> '))
			userC=int(input('Enter number of Cannibals travel=> '))
			if userM==0 and userC==0:
				print('Empty travel not possible\nRe-enter : ')
			elif (userM+userC)<=2 and (rM-userM)>=0 and (rC-userC)>=0:
				break
			else:
				print('Wrong input re-enter : ')
		lM+=userM
		lC+=userC
		rM-=userM
		rC-=userC
		k+=1
		print('')
		for i in range(0,lM):
			print('M ',end='')
		for i in range(0,lC):
			print('C ',end='')
		print('| <-- | ')
		for i in range(0,rM):
			print('M ',end='')
		for i in range(0,rC):
			print('C ',end='')
		print('')
		if (lC==3 and lM==1) or (lC==3 and lM==2) or (lC==2 and lM==1) or (rC==3 and rM==1) or \
			(rC==3 and rM==2) or (rC==2 and rM==1):
			print('Cannibals eat missionaries !\nYou lost the game')
			break
except EOFError as e:
	print('\nInvalid input please retry !!')
