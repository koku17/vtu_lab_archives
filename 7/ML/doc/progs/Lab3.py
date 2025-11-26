import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.utils import resample

X, y = load_iris(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
bag = BaggingClassifier(
    estimator=DecisionTreeClassifier(random_state=0), n_estimators=50, random_state=42
)
bag.fit(X_train, y_train)
y_pred_bag = bag.predict(X_test)

ada = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1, random_state=0),
    n_estimators=100,
    learning_rate=0.5,
    random_state=42,
)
ada.fit(X_train, y_train)
y_pred_ada = ada.predict(X_test)

print(
    "Bagging Accuracy : ",
    accuracy_score(y_test, y_pred_bag),
    "\nBagging Report :\n",
    classification_report(y_test, y_pred_bag),
    "\nBagging Confusion Matrix :\n",
    confusion_matrix(y_test, y_pred_bag),
    "\n\nAdaBoost Accuracy : ",
    accuracy_score(y_test, y_pred_ada),
    "\nAdaBoost Report :\n",
    classification_report(y_test, y_pred_ada),
    "\nAdaBoost Confusion Matrix : \n",
    confusion_matrix(y_test, y_pred_ada),
)

X, y = load_iris(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
n_estimators = 10
models = []

for i in range(n_estimators):
    X_sample, y_sample = resample(X_train, y_train, replace=True, random_state=i)
    model = DecisionTreeClassifier(random_state=i)
    model.fit(X_sample, y_sample)
    models.append(model)




predictions = []
for model in models:
    predictions.append(model.predict(X_test))

predictions = np.array(predictions)
final_predictions = []

for col in predictions.T:
    values, counts = np.unique(col, return_counts=True)
    final_predictions.append(values[np.argmax(counts)])

print("Bagging Accuracy:", accuracy_score(y_test, final_predictions))

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
n_estimators = 10
sample_weights = np.ones(len(X_train)) / len(X_train)
models, alphas = [], []

for i in range(n_estimators):
    model = DecisionTreeClassifier(max_depth=1, random_state=i)
    model.fit(X_train, y_train, sample_weight=sample_weights)
    y_pred = model.predict(X_train)
    err = np.sum(sample_weights * (y_pred != y_train)) / np.sum(sample_weights)

    if err == 0:
        alpha = 1
    else:
        alpha = 0.5 * np.log((1 - err) / (err + 1e-10))

    sample_weights *= np.exp(alpha * (y_pred != y_train))
    sample_weights /= np.sum(sample_weights)
    models.append(model)
    alphas.append(alpha)

final_pred = np.zeros((len(X_test), len(np.unique(y))))

for alpha, model in zip(alphas, models):
    preds = model.predict(X_test)
    for i, p in enumerate(preds):
        final_pred[i, p] += alpha

y_pred_final = np.argmax(final_pred, axis=1)
print("Boosting Accuracy:", accuracy_score(y_test, y_pred_final))
