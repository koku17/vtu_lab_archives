import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler

iris = datasets.load_iris()
X = iris.data
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

class SOM:
    def __init__(
        self, x_dim, y_dim, input_dim, learning_rate=0.5, sigma=None, max_iter=1000
    ):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.input_dim = input_dim
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.sigma = sigma if sigma else max(x_dim, y_dim) / 2
        self.weights = np.random.random((x_dim, y_dim, input_dim))

    def _euclidean_distance(self, x, w):
        return np.linalg.norm(x - w)

    def _find_bmu(self, x):
        min_dist = np.inf
        bmu_idx = (0, 0)
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                dist = self._euclidean_distance(x, self.weights[i, j, :])
                if dist < min_dist:
                    min_dist = dist
                    bmu_idx = (i, j)
        return bmu_idx

    def _update_weights(self, x, bmu_idx, iter_count):
        lr = self.learning_rate * np.exp(-iter_count / self.max_iter)
        sig = self.sigma * np.exp(-iter_count / self.max_iter)
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                dist_to_bmu = np.linalg.norm(np.array([i, j]) - np.array(bmu_idx))
                h = np.exp(-(dist_to_bmu**2) / (2 * sig**2))
                self.weights[i, j, :] += lr * h * (x - self.weights[i, j, :])

    def train(self, data):
        for iter_count in range(self.max_iter):
            for x in data:
                bmu_idx = self._find_bmu(x)
                self._update_weights(x, bmu_idx, iter_count)

    def map_data(self, data):
        mapped = []
        for x in data:
            bmu_idx = self._find_bmu(x)
            mapped.append(bmu_idx)
        return mapped




som = SOM(
    x_dim=5, y_dim=5, input_dim=X_scaled.shape[1], learning_rate=0.5, max_iter=100
)
som.train(X_scaled)
mapped = som.map_data(X_scaled)
print("Mapped BMU indices for data points:\n", mapped)

plt.figure(figsize=(7, 7))
for idx, m in enumerate(mapped):
    plt.text(
        m[0] + 0.5,
        m[1] + 0.5,
        str(idx),
        color=plt.cm.rainbow(iris.target[idx] / 2),
        fontdict={"weight": "bold", "size": 9},
    )
plt.xlim([0, som.x_dim])
plt.ylim([0, som.y_dim])
plt.title("SOM Mapping of Iris Data (Unsupervised)")
plt.show()
