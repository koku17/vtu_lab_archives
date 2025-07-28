import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from scipy.spatial.distance import cdist

df_linear = pd.read_csv('datasets/linear_regdataset.csv')
df_lwr = pd.read_csv('datasets/LWRdataset.csv')
df_poly = pd.read_csv('datasets/poly_regdataset.csv')

def linear_regression(df):
    X,y = df[['X']],df['Y']
    model = LinearRegression()
    model.fit(X,y)
    y_pred = model.predict(X)
    plt.scatter(X,y,label = 'Data')
    plt.plot(X,y_pred,color = 'red', label='Linear Regression')
    plt.legend()
    plt.title('Linear Regression')
    plt.show()
linear_regression(df_linear)

def gaussian_kernel(x, X_train, tau):
    return np.exp(-np.sum((x - X_train)**2, axis=1) / (2 * tau**2))

def locally_weighted_regression(X_train, y_train, tau=0.5):
    X_train = np.hstack([np.ones((X_train.shape[0], 1)), X_train])
    x_range = np.linspace(X_train[:, 1].min(), X_train[:, 1].max(), 100)
    y_pred = []

    for x in x_range:
        x_vec = np.array([1, x])
        weights = gaussian_kernel(x, X_train[:, 1:], tau).flatten()
        W = np.diag(weights)
        theta = np.linalg.pinv(X_train.T @ W @ X_train) @ (X_train.T @ W @ y_train)
        y_pred.append(x_vec @ theta)
    
    plt.scatter(X_train[:, 1], y_train, label='Data')
    plt.plot(x_range, y_pred, color='red', label='LWR')
    plt.legend()
    plt.title('Locally Weighted Regression')
    plt.show()

locally_weighted_regression(df_lwr[['X']].values, df_lwr['Y'].values)

def polynomial_regression(df, degree):
    X, Y = df[['X']], df['Y']
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X, Y)
    y_pred = model.predict(X)
    plt.scatter(X, Y, label='Data')
    plt.plot(X, y_pred, color='red', label=f'Polynomial Regression (deg = {degree})')
    plt.legend()
    plt.title('Polynomial Regression')
    plt.show()

polynomial_regression (df_poly, degree=3)

def gaussian_kernel(x, x_query, tau):
	return np.exp(- (x - x_query) ** 2 / (2 * tau ** 2))

def locally_weighted_regression(X, y, x_query, tau):
	X_b = np.c_[np.ones(len(X)), X]
	x_query_b = np.array([1, x_query])
	W = np.diag(gaussian_kernel(X, x_query, tau))
	theta = np.linalg.inv(X_b.T @ W @ X_b) @ X_b.T @ W @ y
	return x_query_b @ theta

X = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 1.3, 3.75, 2.25])

x_query = 3
tau = 1.0
y_pred = locally_weighted_regression(X, y, x_query, tau)
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Data Points')
plt.scatter(x_query, y_pred, color='red', label=f'Prediction at x={x_query}')
weights = gaussian_kernel(X, x_query, tau)

for i in range(len(X)):
	plt.plot([X[i], X[i]], [y[i], y[i] - weights[i]], 'k-', lw=1)
	plt.scatter(X[i], y[i], s=weights[i] * 200, color='green', alpha=0.5)
	plt.title('Locally Weighted Regression (LWR)')
	plt.xlabel('X')
	plt.ylabel('Y')

plt.legend()
plt.show()

def locally_weighted_regression(X, y, x_query, tau):
	X_b = np.c_[np.ones(len(X)), X]
	x_query_b = np.array([1, x_query])
	W = np.diag(gaussian_kernel(X, x_query, tau))
	theta = np.linalg.pinv(X_b.T @ W @ X_b) @ X_b.T @ W @ y
	return x_query_b @ theta

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 3, 2, 4, 3.5, 5, 6, 7, 6.5, 8])
X_query = np.linspace(1, 10, 100)
tau = 1.0
y_lwr = np.array([locally_weighted_regression(X, y, x_q, tau) for x_q in X_query])
lin_reg = LinearRegression()
X_reshaped = X.reshape(-1, 1)
lin_reg.fit(X_reshaped, y)
y_lin = lin_reg.predict(X_query.reshape(-1, 1))
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot (X_query, y_lin, color='black', linestyle='dashed', label='Simple Linear Regression')
plt.plot (X_query, y_lwr, color='red', label='Locally Weighted Regression')
plt.title ('Comparison: Simple Linear Regression vs. Locally Weighted Regression')
plt.xlabel ('X')
plt.ylabel ('Y')
plt.legend()
plt.show()

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 3, 2, 4, 3.5, 5, 6, 7, 6.5, 8])
X_query = np.linspace(1, 10, 100)
tau_values = [0.1, 0.5, 1.0, 5.0, 10.0]
lin_reg = LinearRegression()
X_reshaped = X.reshape(-1, 1)
lin_reg.fit(X_reshaped, y)
y_lin = lin_reg.predict(X_query.reshape(-1, 1))
plt.figure(figsize=(12, 8))
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X_query, y_lin, color='black', linestyle='dashed', label='Simple Linear Regression')
colors = ['red', 'green', 'purple', 'orange', 'brown']
for tau, color in zip(tau_values, colors):
	y_lwr = np.array([locally_weighted_regression(X, y, x_q, tau) for x_q in X_query])
	plt.plot(X_query, y_lwr, color=color, label=r'LWR ($\tau$={tau})')
	plt.title(r'Effect of Different $\tau$ Values in Locally Weighted Regression')
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.legend()

plt.show()
