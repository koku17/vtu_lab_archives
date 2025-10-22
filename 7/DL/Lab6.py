import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("datasets/airline-passengers.csv", usecols=[1])
data = df.values.astype("float32")
scaler = MinMaxScaler()
data = scaler.fit_transform(data)


def create_dataset(dataset, look_back=3):
    X, Y = [], []
    for i in range(len(dataset) - look_back - 1):
        X.append(dataset[i : i + look_back, 0])
        Y.append(dataset[i : i + look_back, 0])
    return np.array(X), np.array(Y)


look_back = 3
X, y = create_dataset(data, look_back)
model = Sequential([LSTM(50, input_shape=(look_back, 1)), Dense(1)])
model.compile(loss="mean_squared_error", optimizer="adam")
model.fit(X, y, epochs=100, batch_size=1, verbose=0)

predicted = model.predict(X)
predicted = scaler.inverse_transform(predicted)
actual = scaler.inverse_transform(y.reshape(-1, 1))
print(predicted, actual, sep="\n")

plt.figure(figsize=(10, 6))
plt.plot(actual, label="Actual Data", color="blue")
plt.plot(predicted, label="Predicted Data", color="red")
plt.title("Airline Passengers Prdictoin")
plt.xlabel("Time Steps")
plt.ylabel("Passengers")
plt.legend()
plt.show()
