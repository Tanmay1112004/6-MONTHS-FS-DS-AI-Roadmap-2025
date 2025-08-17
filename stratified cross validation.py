# -*- coding: utf-8 -*-
"""
Stratified K-Fold Cross Validation
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression

# Load data
dataset = pd.read_csv(r"C:\Users\Mukesh\OneDrive\Desktop\Tanmay Folder\logit classification.csv")
X = dataset.iloc[:, [2, 3]].values  # Update column indices
y = dataset.iloc[:, -1].values

# Initialize model
model = LogisticRegression(max_iter=1000, random_state=42)

# Stratified 5-Fold CV
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf, scoring='accuracy')

# Results
print("Stratified K-Fold CV Results (5 folds):")
print(f"Mean Accuracy: {scores.mean():.4f}")
print(f"Standard Deviation: {scores.std():.4f}")
print("\nIndividual Fold Accuracies:", [f"{x:.4f}" for x in scores])