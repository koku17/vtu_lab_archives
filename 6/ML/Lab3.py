import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = datasets.load_iris ()
x = iris.data
y = iris.target

scaler = StandardScaler ()
x_scaled = scaler.fit_transform (x)

cov_matrix = np.cov (x_scaled.T)
eigenvalues, eigenvectors = np.linalg.eig (cov_matrix)

print (x, y, x_scaled, sep = '\n\n')
print (
	'\nCovariance Matrix :', cov_matrix,
	'\nEigen Values :', eigenvalues,
	'\nEigen Vectors :', eigenvectors,
	sep='\n'
)

fig = plt.figure (figsize = (8,6))
ax = fig.add_subplot (111, projection = '3d')
colors = ['red', 'green', 'blue']
labels = iris.target_names
for i in range (len (colors)):
	ax.scatter (
		x_scaled[y == i, 0],
		x_scaled[y == i, 1],
		x_scaled[y == i, 2],
		color = colors[i],
		label = labels[i]
	)
ax.set_xlabel ('Sepal Length')
ax.set_ylabel ('Sepal Width')
ax.set_zlabel ('Petal Length')
ax.set_title ('3D Visualization of iris data before PCA')
plt.legend ()
plt.show ()

U, S, Vt = np.linalg.svd (x_scaled, full_matrices = False)
pca = PCA (n_components = 2)
x_pca = pca.fit_transform (x_scaled)
explained_variance = pca.explained_variance_ratio_

print (
	'\nSingular Values :', S,
	'\nReduced Dimensions :', x_pca,
	f'\nExplained Variance by PCA1 : {explained_variance[0]:.2f}',
	f'Explained Variance by PCA2 : {explained_variance[1]:.2f}',
	sep='\n'
)

for i in range (len (colors)):
	plt.scatter (
		x_pca[y == i, 0],
		x_pca[y == i, 1],
		color = colors[i],
		label = labels[i]
	)
plt.xlabel ('Principle Component 1')
plt.ylabel ('Principle Component 2')
plt.title ('PCA on Iris Dataset (Dimensionality Reduction)')
plt.legend ()
plt.grid ()
plt.show ()

fig = plt.figure (figsize = (8,6))
ax = fig.add_subplot (111, projection = '3d')
for i in range (len (colors)):
	ax.scatter (
		x_scaled[y == i, 0],
		x_scaled[y == i, 1],
		x_scaled[y == i, 2],
		color = colors[i],
		label = labels[i]
	)
for i in range (3):
	ax.quiver (0, 0, 0, eigenvectors[i, 0], eigenvectors[i, 1], eigenvectors[i, 2])
ax.set_xlabel ('Sepal Length')
ax.set_ylabel ('Sepal Width')
ax.set_zlabel ('Petal Length')
ax.set_title ('3D Data with Eigenvectors')
plt.legend ()
plt.show ()
