import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df=sns.load_dataset('titanic')
df

print(
	"\n Basic Information about dataset:",df.info(),
	"\n Summary Statistics:",df.describe(),
	"\nMissing values in each column",df.isnull().sum()
)

columns_remove=['deck','embarked','alive','pclass']
df=df.drop(columns=columns_remove)

df['age'].fillna(round(df['age'].mean()),inplace=True)
df['embark_town'].mode()[0]
df['embark_town'].fillna(df['embark_town'].mode()[0],inplace=True)

df.isnull().sum()

df.duplicated().sum()
df.drop_duplicates(inplace=True)
df.duplicated().sum()

plt.figure(figsize=(12,8))
df.hist(figsize=(12,8),bins=30,edgecolor='black')
plt.suptitle("Feature Distribution",fontsize=16)
plt.savefig('feature_distribution.svg')
plt.show()

plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.xticks(rotation=45)
plt.title("Boxplots of Features to Identify Outliers")
plt.savefig('outliers.svg')
plt.show()

num_col=df.select_dtypes(include=[np.number]).columns.tolist()
cat_col=df.select_dtypes(include=['object']).columns
print(f"numerical_data: {num_col}")

plt.figure(figsize=(8,6))
sns.scatterplot(x=df['age'],y=df['fare'])
plt.title("Scatter plot: Age vs Fare")
plt.xlabel("Age")
plt.ylabel("fare")
plt.savefig('scatter_plot.svg')
plt.show()

sns.pairplot(df,diag_kind='kde')
plt.savefig('kde.svg')
plt.show()

correlation=df[['age','fare']].corr('pearson')
covariance=df[['age','fare']].cov()
print(
	"pearson correlation coefficient:\n",correlation,
	"Covariance matrix:\n",covariance
)

plt.figure(figsize=(10,6))
corr_matrix=df[num_col].corr('pearson')
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',fmt='.2f')
plt.title("Feature correlation heatmap")
plt.savefig('heatmap.svg')
plt.show()

df=sns.load_dataset('iris')
df

print(
	"\n Basic Information about dataset:",df.info(),
	"\n Summary Statistics:",df.describe(),
	"Missing values in each column",df.isnull().sum()
)

df.columns
columns_remove = ['sepal_length', 'species']
df=df.drop(columns=columns_remove)
