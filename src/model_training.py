from xgboost import XGBClassifier
from sklearn.impute import SimpleImputer


def split_data(X, y, test_size=0.2, random_state=42):
    from sklearn.model_selection import train_test_split
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def train_model(X_train, y_train):

    imputer = SimpleImputer(strategy="most_frequent")
    X_train_clean = imputer.fit_transform(X_train)

    model = XGBClassifier(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=5,
        subsample=0.8,
        colsample_bytree=0.7,
        gamma=5,
        random_state=42,
        eval_metric="logloss"
    )

    model.fit(X_train_clean, y_train)

    return model, imputer


def evaluate_model(model, imputer, X_test, y_test):

    from sklearn.metrics import classification_report

    BEST_THRESHOLD = 0.3

    X_test_clean = imputer.transform(X_test)

    y_proba = model.predict_proba(X_test_clean)[:, 1]
    y_pred = (y_proba >= BEST_THRESHOLD).astype(int)

    print(classification_report(y_test, y_pred))