import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
iris = sns.load_dataset('iris')
iris.head()

iris.shape
print ('Basic Information about the dataset')
iris.info()
iris.hist(figsize=(12,8), bins=30, edgecolor='black')
plt.suptitle('Feature Distribution', fontsize=16)
plt.show()

plt.figure(figsize=(12,6))
sns.boxplot(data=iris)
plt.xticks(rotation=45)
plt.title('Boxplots of features to identify outliers')
plt.show()

num_col = iris.select_dtypes(include=[np.number]).columns
cat_col = iris.select_dtypes(include=['object']).columns
plt.figure(figsize=(10, 6))
corr_matrix=iris[num_col].corr('pearson')
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.suptitle('Feature Correlation heatmap', fontsize=16)
plt.show()

label_encoder = LabelEncoder()
iris['species']=label_encoder.fit_transform(iris['species'])
X=iris.drop(['species'],axis=1)
y=iris['species']
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)
y_pred = nb_classifier.predict(X_test)
y_pred
accuracy = accuracy_score (y_test, y_pred)
print (
    f'Accuracy : {accuracy:.2f}',
    '\nClassification Report :', classification_report(y_test, y_pred),
    '\nConfusion Matrix : ', confusion_matrix(y_test, y_pred), sep = '\n'
)

plt.figure(figsize=(6,4))
sns.heatmap(
    confusion_matrix(y_test, y_pred),
    annot=True, cmap='Blues',
    fmt='d', xticklabels = iris.keys(),
    yticklabels=iris.keys()
)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
