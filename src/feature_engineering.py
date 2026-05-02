import pandas as pd


def encode_target(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Churn"] = df["Churn"].astype(str).str.strip()
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    return df


def encode_binary_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "gender" in df.columns:
        df["gender"] = df["gender"].map({"Male": 1, "Female": 0})

    binary_cols = [
        "Partner", "Dependents", "PhoneService", "PaperlessBilling",
        "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies"
    ]

    for col in binary_cols:
        if col in df.columns:
            df[col] = df[col].map({"Yes": 1, "No": 0})

    return df


def encode_categorical_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    obj_cols = df.select_dtypes(include="object").columns
    obj_cols = [c for c in obj_cols if c != "Churn"]

    df = pd.get_dummies(df, columns=obj_cols, drop_first=True)

    return df


def transform_features(df: pd.DataFrame) -> pd.DataFrame:
    df = encode_target(df)
    df = encode_binary_columns(df)
    df = encode_categorical_columns(df)

    # final safety
    df = df.dropna()

    return df