import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings

warnings.filterwarnings ('ignore')

from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing ()
Data = pd.DataFrame (housing.data, columns = housing.feature_names)
Data.info ()

Numerical = Data.select_dtypes (include = [np.number]).columns
for i in Numerical:
	print (
		f'Statistics for columns {i}',
		f'\nMean : ', Data[i].mean (),
		f'\nMedian : ', Data[i].median (),
		f'\nMode : ', Data[i].mode ()[0],
		f'\nStandard Deviation : ', Data[i].std (),
		f'\nVariance : ', Data[i].var (),
		f'\nRange : ', Data[i].max () - Data[i].min (),
		sep=' ', end='\n\n'
	)

Data.isnull ().sum ()

print (Numerical)

plt.figure (figsize = (5,5))
plt.ylabel ('Frequency')

for i in Numerical:
	Data[i].plot (kind = 'hist', title = i, bins = 50, edgecolor = 'black')
	plt.show ()

for i in Numerical:
	sns.boxplot (Data[i], color = 'green')
	plt.title (i)
	plt.ylabel (i)
	plt.show ()
	

data=Data
def detect_outliers_iqr(Data):
	outliers={}
 
	for i in Data.columns:
		q1=np.percentile(Data[i],25)
		q3=np.percentile(Data[i],75)
		iqr=q3-q1
		lower_bound=q1-1.5*iqr
		upper_bound=q3+1.5*iqr
		outlier_values=data[(data[i]<lower_bound)| (data[i]>upper_bound)][i]
		outliers[i]=outlier_values.tolist()
	return outliers
outliers_dict=detect_outliers_iqr(Data)

for feature,outliers in outliers_dict.items():
	print(f'{feature} : {len(outliers)} outliers found')

np.random.seed (42)
numerical_data = np.random.randint (20, 80, size=95).tolist ()
outliers = [150, 160, 170, 5, 10]
numerical_data.extend (outliers)
categories = ['A', 'B', 'C', 'D']
categorical_data = np.random.choice (categories, size=100)
Data = pd.DataFrame ({
'numerical_column': numerical_data,
'categorical_column': categorical_data
})
cat_col = Data.select_dtypes(include=['object']).columns
category_counts = Data[cat_col].value_counts()
plt.figure(figsize=(8,5))
category_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie Chart of Categories')
plt.ylabel('')
plt.show()
