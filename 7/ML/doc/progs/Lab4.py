import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X, _ = load_iris(return_X_y=True, as_frame=True)
X_scaled = StandardScaler().fit_transform(X)
kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
labels = kmeans.fit_predict(X_scaled)

# visulalization
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(
    X_scaled[:, 0], X_scaled[:, 1], X_scaled[:, 2], c=labels, cmap="viridis", s=50
)

ax.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    kmeans.cluster_centers_[:, 2],
    c="red",
    marker="X",
    s=200,
    label="Centroid",
)

ax.set_title("K-Means Clustring on Unlabeled Iris Data (3D View)")
ax.set_xlabel("Feature 0")
ax.set_ylabel("Feature 1")
ax.set_zlabel("Feature 2")
plt.legend()
plt.show()

sil = silhouette_score(X_scaled, labels)
print(
    "Silhouette Score : ",
    sil,
    "\nCluster Centers (in scaled space) : \n",
    kmeans.cluster_centers_,
)
