# GridSearchCV Example

from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Model
model = SVC()

# Hyperparameter grid
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 'auto']
}

# Grid Search
grid = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    verbose=2
)

# Train
grid.fit(X, y)

# Results
print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)
