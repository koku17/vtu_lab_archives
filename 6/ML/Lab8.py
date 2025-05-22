import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import export_graphviz
from IPython.display import Image
import pydotplus
import warnings

warnings.filterwarnings("ignore")
data = pd.read_csv("datasets/titanic.csv")
data.head()
pd.set_option("display.max_columns", None)
data.isnull().sum()
df = data.drop(["cabin"], axis=1)
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
df.isnull().sum()
df = df.drop(columns=["passenger_id", "sibsp", "parch", "ticket", "name"])
df.columns

# Encode categorical variables
df = pd.get_dummies(df, columns=["sex", "embarked", "pclass"], drop_first=True)

# select features and target
X = df.drop(
    columns=[
        "survived",
        "home.dest",
        "embarked_Q",
        "embarked_S",
        "pclass_2",
        "pclass_3",
        "sex_male",
        "boat",
    ]
)
y = df["survived"]
for col in X.columns:
    print(f"{col}: {X[col].unique()}")

# split tinto trainik ng AND TESTING
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=True
)

dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)

# export to DOT format
dot_data = export_graphviz(
    dt,
    out_file=None,
    feature_names=X_train.columns,
    rounded=True,
    proportion=False,
    precision=2,
    filled=True,
)

# converting Dot to graph
graph = pydotplus.graph_from_dot_data(dot_data)

Image(graph.create_png())
with open("dot_data_tree.svg", "w") as f:
    f.write(graph.create_svg().decode("utf-8"))

plt.figure(figsize=(12, 8))
plot_tree(
    dt, filled=True, feature_names=X.columns, class_names=["survived", "unsurvived"]
)

plt.show()
