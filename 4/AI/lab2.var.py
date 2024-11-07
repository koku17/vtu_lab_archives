#!/bin/python

print(
	'Game Start \
	\nNow the task is to move all of them to right side of the river \
	\nRules : \
	\n1. The boat can carry at most two people \
	\n2. If cannibals number greater than missionaries then the cannibals would eat the missionaries \
	\n3. The boat cannot cross the river by itself with no people on board'
)

lM=3
lC=3
rM=0
rC=0
uM=0
uC=0
k=0

def IN():
	M=int(input('Enter number of Missionaries travel => '))
	C=int(input('Enter number of Cannibals travel => '))
	return M,C

def POS(direction):
	print('')
	for i in range(0,lM):
		print('M ',end='')
	for i in range(0,lC):
		print('C ',end='')
	if direction==0:
		print('| --> | ',end='')
	elif direction==1:
		print('| <-- | ',end='')
	for i in range(0,rM):
		print('M ',end='')
	for i in range(0,rC):
		print('C ',end='')
	print('\n')

def WIN():
	if rM+rC==6:
		print('You won the game : \nCongrats !')
		print('Total attempts : ',k)
		exit(0)
try:
	POS(0)
	while(True):
		while(True):
			print('Left side -> right side river travel')
			uM,uC=IN()
			if uM==0 and uC==0:
				print('Empty travel not possible, Re-enter : ')
			elif (uM+uC)<=2 and (lM-uM)>=0 and (lC-uC)>=0:
				break
			else:
				print('Wrong input re-enter : ')
		lM-=uM
		lC-=uC
		rM+=uM
		rC+=uC
		k+=1
		POS(0)
		if lC>lM and lM>0 or rC>rM and rM>0:
			print('Cannibals eat missionaries !\nYou lost the game !')
			exit(1)
		WIN()
		while(True):
			print('Right side -> Left side river travel')
			uM,uC=IN()
			if uM==0 and uC==0:
				print('Empty travel not possible, Re-enter : ')
			elif (uM+uC)<=2 and (rM-uM)>=0 and (rC-uC)>=0:
				break
			else:
				print('Wrong input re-enter : ')
		lM+=uM
		lC+=uC
		rM-=uM
		rC-=uC
		k+=1
		POS(1)
		if rC>rM and rM>0 or lC>lM and lM>0:
			print('Cannibals eat missionaries !\nYou lost the game !')
			exit(1)
		WIN()
except EOFError as e:
	print('\nInvalid input please retry !')
