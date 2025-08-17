# -*- coding: utf-8 -*-
"""
K-Fold Cross Validation
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier

# Load data
dataset = pd.read_csv(r"C:\Users\Mukesh\OneDrive\Desktop\Tanmay Folder\logit classification.csv")
X = dataset.iloc[:, [2, 3]].values  # Update column indices
y = dataset.iloc[:, -1].values

# Initialize model
model = RandomForestClassifier(random_state=42)

# 5-Fold CV
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')

# Results
print("K-Fold CV Results (5 folds):")
print(f"Mean Accuracy: {scores.mean():.4f}")
print(f"Standard Deviation: {scores.std():.4f}")
print("\nIndividual Fold Accuracies:", [f"{x:.4f}" for x in scores])