from sklearn.datasets import load_iris
from sklearn.model_selection import RandomizedSearchCV
from sklearn.svm import SVC
import numpy as np

# Load data
data = load_iris()
X = data.data
y = data.target

# Model
model = SVC()

# Parameter distribution
param_dist = {
    'C': np.logspace(-3, 3, 10),
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 'auto']
}

# Random Search
random_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_dist,
    n_iter=5,
    cv=5,
    scoring='accuracy',
    verbose=2,
    random_state=42
)

# Train
random_search.fit(X, y)

# Results
print("Best Parameters:", random_search.best_params_)
print("Best Score:", random_search.best_score_)
