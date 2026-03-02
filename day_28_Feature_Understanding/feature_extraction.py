import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA

# -----------------------------
# Example 1: Categorical Encoding
# -----------------------------

df = pd.read_csv("data/sample_data.csv")

encoder = OneHotEncoder(sparse_output=False)

city_encoded = encoder.fit_transform(df[["city"]])

encoded_df = pd.DataFrame(
    city_encoded,
    columns=encoder.get_feature_names_out(["city"])
)

df = pd.concat([df, encoded_df], axis=1)

print("===== One Hot Encoded Data =====")
print(df.head())

# -----------------------------
# Example 2: Text Feature Extraction
# -----------------------------

documents = [
    "machine learning is powerful",
    "deep learning is part of machine learning",
    "python is used for machine learning"
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

print("\n===== TF-IDF Features =====")
print(vectorizer.get_feature_names_out())
print(tfidf_matrix.toarray())

# -----------------------------
# Example 3: Dimensionality Reduction (PCA)
# -----------------------------

pca = PCA(n_components=2)

numeric_data = df[["age", "income", "experience"]]

pca_features = pca.fit_transform(numeric_data)

print("\n===== PCA Reduced Features =====")
print(pca_features)
