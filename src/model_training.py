from lightgbm import LGBMClassifier
from sklearn.impute import SimpleImputer


def split_data(X, y, test_size=0.2, random_state=42):
    from sklearn.model_selection import train_test_split
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def train_model(X_train, y_train):

    imputer = SimpleImputer(strategy="most_frequent")

    X_train_clean = imputer.fit_transform(X_train)

    model = LGBMClassifier(
        n_estimators=300,
        learning_rate=0.05,
        random_state=42
    )

    model.fit(X_train_clean, y_train)

    return model, imputer


def evaluate_model(model, imputer, X_test, y_test):

    from sklearn.metrics import classification_report

    X_test_clean = imputer.transform(X_test)

    y_pred = model.predict(X_test_clean)

    print(classification_report(y_test, y_pred))