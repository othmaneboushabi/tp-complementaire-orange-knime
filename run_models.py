from pathlib import Path

import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


df = pd.read_csv("data/transactions.csv")
X = df.drop(columns="fraude")
y = df["fraude"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "kNN normalise": make_pipeline(StandardScaler(), KNeighborsClassifier()),
    "Tree": __import__("sklearn.tree", fromlist=["DecisionTreeClassifier"]).DecisionTreeClassifier(
        random_state=42
    ),
    "Random Forest": RandomForestClassifier(
        n_estimators=100, random_state=42, n_jobs=-1
    ),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42),
}

Path("reports").mkdir(exist_ok=True)
rows = []
for name, model in models.items():
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    rows.append((name, f1_score(y_test, prediction)))
    if name == "Gradient Boosting":
        print("Gradient Boosting confusion matrix:")
        print(confusion_matrix(y_test, prediction, labels=[0, 1]))

print("Results:")
for name, score in rows:
    print(f"{name}: F1 classe 1 = {score:.4f}")
