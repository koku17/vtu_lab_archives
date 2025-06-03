import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

data = pd.read_csv('../../datasets/bcancer.csv')
print(
	data.head(),
	data.shape,
	data.info(),
	data.diagnosis.unique(),
	data.isnull().sum(),
	data.duplicated().sum(), sep = '\n'
)

#df = data.drop(['id', 'Unnamed: 32'], axis=1)
df = data
df['diagnosis'] = df['diagnosis'].map({'M':1, 'B':0})
print (df.describe().T)

#df.drop(columns=['diagnosis'], axis=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)
pca = PCA(n_components=2)
x_pca = pca.fit_transform(df)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
explained_variance = pca.explained_variance_ratio_
total_explained_variance = np.sum(explained_variance)
print(
    f'Variance explained by PC1 : {explained_variance[0]:.4f}',
    f'Variance explained by PC2 : {explained_variance[1]:.4f}',
    f'Total variance explained by first 2 components : {total_explained_variance:.4f}',
    sep = '\n'
)

wcss = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_pca)
    wcss.append(kmeans.inertia_)
plt.figure(figsize=(8, 5))
plt.plot(K_range, wcss, marker="o", linestyle="-")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("WCSS")
plt.title("Elbow Method to Find Optimal k")
plt.savefig('elbow_optimal.svg')
plt.show()

optimal_k = 2
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_pca)
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap="viridis", alpha=0.6)
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=200, c='red'
)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("K-Means Clustering after PCA")
plt.grid()
plt.savefig('k_means_pca.svg')
plt.show()
