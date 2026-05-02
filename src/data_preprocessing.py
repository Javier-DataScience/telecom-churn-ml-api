import pandas as pd


def load_and_clean_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    return df


def prepare_data(df: pd.DataFrame):
    X = df.drop("Churn", axis=1)
    y = df["Churn"]
    return X, y