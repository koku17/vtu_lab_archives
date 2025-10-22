import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

vocab_size = 5000
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=vocab_size)
maxlen = 500
x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

model = Sequential(
    [
        Embedding(vocab_size, 128, input_length=maxlen),
        LSTM(100),
        Dense(1, activation="sigmoid"),
    ]
)

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))

loss, acc = model.evaluate(x_test, y_test)
print(f"Test Accuracy : {acc:.4f}")

y_pred = model.predict(x_test)
for i in range(5):
    print(f"Review {i+1} : Predicted = {y_pred[i][0]} Actual = {y_test[1]}")

y_pred_prob = model.predict(x_test)
y_pred = (y_pred_prob > 0.5).astype("int32")
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm, display_labels=["Negative", "Positive"]
)
disp.plot(cmap="Blues")
plt.title("Confusion Matrix for IMDB Sentiment Classification")
plt.show()
