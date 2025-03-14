import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def min_edit_distance (str1, str2):
	m, n = len (str1), len (str2)
	dp = np.zeros ((m + 1, n + 1), dtype = int)

	for i in range (m + 1):
		for j in range (n + 1):
			if i == 0:
				dp[i][j] = j
			elif j == 0:
				dp[i][j] = i
			elif str1[i - 1] == str2[j - 1]:
				dp[i][j] = dp[i - 1][j - 1]
			else:
				dp[i][j] = 1 + min (dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
	return dp[m][n]
			 
test_cases = [
	('hello', 'helo'),
	('hello', 'heloo'),
	('hello', 'hallo'),
	('hello', 'world'),
	('intention', 'execution'),
]

results = []

for str1, str2 in test_cases:
	med = min_edit_distance (str1, str2)
	results.append ((str1, str2, med))
	
print (pd.DataFrame (results, columns = ['string1', 'string2', 'Min Edit distance']).to_string (index = False))
