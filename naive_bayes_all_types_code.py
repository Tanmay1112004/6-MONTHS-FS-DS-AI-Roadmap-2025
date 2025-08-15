import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, Normalizer
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# ---------------- Load Dataset ----------------
dataset = pd.read_csv(r"C:\Users\Mukesh\OneDrive\Desktop\Tanmay Folder\logit classification.csv")

# Features & Target
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values

# ---------------- Train-Test Split ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0
)

# ---------------- Preprocessing ----------------
scaler = StandardScaler()
normalizer = Normalizer()

X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

X_train_norm = normalizer.fit_transform(X_train)
X_test_norm = normalizer.transform(X_test)

# ---------------- Models Dictionary ----------------
models = {
    "BernoulliNB (No Scaling)": (BernoulliNB(), X_train, X_test),
    "BernoulliNB (StandardScaler)": (BernoulliNB(), X_train_std, X_test_std),
    "BernoulliNB (Normalizer)": (BernoulliNB(), X_train_norm, X_test_norm),

    "GaussianNB (No Scaling)": (GaussianNB(), X_train, X_test),
    "GaussianNB (StandardScaler)": (GaussianNB(), X_train_std, X_test_std),
    "GaussianNB (Normalizer)": (GaussianNB(), X_train_norm, X_test_norm),

    "MultinomialNB (No Scaling)": (MultinomialNB(), X_train, X_test),  # non-negative raw
    "MultinomialNB (Normalizer)": (MultinomialNB(), X_train_norm, X_test_norm),  # non-negative norm
}

# ---------------- Training & Evaluation ----------------
results = []

for name, (model, Xtr, Xte) in models.items():
    print(f"\n===== {name} =====")
    try:
        model.fit(Xtr, y_train)
        y_pred = model.predict(Xte)

        cm = confusion_matrix(y_test, y_pred)
        print("Confusion Matrix:\n", cm)

        ac = accuracy_score(y_test, y_pred)
        print("Accuracy:", round(ac, 4))

        cr = classification_report(y_test, y_pred)
        print("Classification Report:\n", cr)

        train_score = model.score(Xtr, y_train)
        test_score = model.score(Xte, y_test)
        print("Training Score (Variance):", round(train_score, 4))
        print("Test Score (Bias):", round(test_score, 4))

        results.append([name, round(ac, 4), round(train_score, 4), round(test_score, 4)])
    except ValueError as e:
        print(f"Skipped due to error: {e}")
        results.append([name, None, None, None])

# ---------------- Summary Table ----------------
df_results = pd.DataFrame(results, columns=["Model", "Accuracy", "Train Score", "Test Score"])
print("\n=== Summary of All Models ===")
print(df_results)
