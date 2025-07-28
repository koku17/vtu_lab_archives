import pandas as pd

data = pd.read_csv ('datasets/training_data.csv')
print (data)

def find_s_algorithm (data):
	attributes = data.iloc[:, :-1].values
	target = data.iloc[:, -1].values
	for i in range (len (target)):
		if target[i] == 'Yes':
			hypothesis = attributes[i].copy ()
			break
	for i in range (len (target)):
		if target[i] == 'Yes':
			for j in range (len (hypothesis)):
				if hypothesis[j] != attributes[i][j]:
					hypothesis[j] = '?'
	return hypothesis

print ('\nMost Specific Hypothesis : ', find_s_algorithm (data))
