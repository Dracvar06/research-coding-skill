import numpy as np
from scipy.stats import binomtest
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X = np.load("data/features.npy")  # (samples, features)
y = np.load("data/labels.npy")    # 0 = condition A, 1 = condition B

clf = make_pipeline(StandardScaler(), SelectKBest(f_classif, k=20),
                    LogisticRegression(C=1.0, max_iter=1000))

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
pred = cross_val_predict(clf, X, y, cv=cv)

n_correct = int((pred == y).sum())
acc = n_correct / len(y)
p = binomtest(n_correct, len(y), 0.5, alternative="greater").pvalue
print(f"Decoding accuracy: {acc:.3f} ({n_correct}/{len(y)})")
print(f"Binomial test vs chance: p = {p:.2e}")
