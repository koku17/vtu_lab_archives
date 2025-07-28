import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
import warnings

warnings.filterwarnings("ignore")

df=pd.read_csv("datasets/Boston housing dataset.csv")

print (
	df.describe(),
	df['CHAS'],
	df.duplicated().sum(), sep = '\n'
)

df['CRIM'].fillna(df['CRIM'].mean(),inplace=True)
df['ZN'].fillna(df['ZN'].mean(),inplace=True)
df['CHAS'].fillna(df['CHAS'].mode()[0],inplace=True)
df['INDUS'].fillna(df['INDUS'].mean(),inplace=True)
df['AGE'].fillna(df['AGE'].median(),inplace=True)
df['LSTAT'].fillna(df['LSTAT'].median(),inplace=True)
df['CHAS']=df['CHAS'].astype('int')

plt.figure(figsize = (6, 3))
for i in df.columns:
	df[i].hist(bins = 20, alpha = 0.5, color = 'b', edgecolor = 'black')
	plt.title(f'Histogram of {i}')
	plt.xlabel(i)
	plt.ylabel('Frequency')
	plt.boxplot(df[i], vert = False)
	plt.title(f'Boxplot of {i}')
	plt.show()

plt.figure(figsize=(10, 8))
corr = df.corr(method='pearson')
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.xticks(rotation=98, ha='right')
plt .yticks(rotation=0)
plt.title("Correlation Matrix Heatmap")
plt.show()

X = df.drop("MEDV", axis=1)
y = df['MEDV']
scale = StandardScaler()
X_scaled = scale. fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print(
	f'Mean Squared Error: {mse}',
	f'Root Mean Squared Error: {rmse}',
	f'R-squared: {r2}', sep = '\n'
)

sns.get_dataset_names()
data = sns.load_dataset('mpg')

print (
	data.head(),
	data.shape,
	data.nunique(),
	data.horsepower.unique(),
	data.isnull().sum(),
	data.duplicated().sum(), sep = '\n'
)

df = data.copy()
df['horsepower'].fillna(df['horsepower'].median(), inplace=True)
numerical = df.select_dtypes(include=['int','float']).columns
categorical = df.select_dtypes(include=['object']).columns
print (
	df.describe().T,
	numerical,
	categorical, sep = '\n'
)

for i in numerical:
	plt.figure(figsize=(10,4))
	plt.subplot(1, 2, 1)
	df[i].hist(bins=20, alpha=0.5, color='b',edgecolor='black')
	plt.title(f'Histogram of {i}')
	plt.xlabel(i)
	plt.ylabel('Frequency')
	plt.subplot(1, 2, 2)
	plt.boxplot(df[i], vert=False)
	plt.title(f'Boxplot of {i}')
	plt.show()

for col in categorical:
	plt.figure(figsize=(6, 6))
	sns.countplot(
		x=col, data=df, order=df[col].value_counts().sort_values().head(1)
	)
	plt.title(f'Countplot of {col}')
	plt.xticks(rotation=90)
	plt.show()

corr_data = df[numerical].corr(method='pearson')
plt.figure(figsize=(10, 8))
sns.heatmap(corr_data, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.xticks(rotation=90, ha='right')
plt.yticks(rotation=0)
plt.title("Correlation Matrix Heatmap")
plt.show()

X = df[['horsepower']]
y = df['mpg']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
degree = 2
poly = PolynomialFeatures(degree)
X_poly_train = poly.fit_transform(X_train)
model = LinearRegression()
model.fit(X_poly_train, y_train)
X_poly_test = poly.transform(X_test)
y_pred = model.predict(X_poly_test)
plt.scatter(X, y, color='blue', label='Data')
X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
X_range_poly = poly.transform(X_range)
y_range_pred = model.predict(X_range_poly)
plt.plot(X_range, y_range_pred, color='red', label='Polynomial Fit')
plt.xlabel('Horsepower')
plt.ylabel('MPG')
plt.legend()
plt.title(f'Polynomial Regression (degree {degree})')
plt.show()

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print (
	f'Mean Squared Error (MSE): {mse:.2f}',
	f'Root Mean Squared Error (RMSE): {rmse:.2f}',
	f'R-squared (R$^2$): {r2:.2f}', sep = '\n'
)
