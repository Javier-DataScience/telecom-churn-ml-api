from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report


def split_data(X, y):
    return train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )


def train_model(X_train, y_train):
    imputer = SimpleImputer(strategy="most_frequent")

    X_train = imputer.fit_transform(X_train)

    model = LogisticRegression(max_iter=2000)
    model.fit(X_train, y_train)

    return model, imputer


def evaluate_model(model, imputer, X_test, y_test):
    X_test = imputer.transform(X_test)

    y_pred = model.predict(X_test)

    print(classification_report(y_test, y_pred))