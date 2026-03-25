from sklearn.model_selection import train_test_split

def preprocess_data(df):
    df = df.copy()

    # Select useful columns
    cols = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Survived']
    df = df[cols]

    # Fill missing values
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

    # Encode categorical columns
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

    # Split features and target
    X = df.drop('Survived', axis=1)
    y = df['Survived']

    return train_test_split(X, y, test_size=0.2, random_state=42)
