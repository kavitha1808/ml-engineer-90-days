import time
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Without optimization
start = time.time()
model = RandomForestClassifier()
model.fit(X_train, y_train)
end = time.time()

print("Training Time (default):", end - start)

# With optimization
start = time.time()
model_opt = RandomForestClassifier(n_estimators=50, max_depth=5, n_jobs=-1)
model_opt.fit(X_train, y_train)
end = time.time()

print("Training Time (optimized):", end - start)
