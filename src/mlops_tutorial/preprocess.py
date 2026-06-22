# import library
import pandas as pd
from sklearn.model_selection import train_test_split

from mlops_tutorial.data import load_data
from mlops_tutorial.config import TRAIN_FILE, TEST_FILE


def preprocess_data():
    # load arw data
    df = load_data()

    # remove customerID
    df.drop(columns=["customerID"], inplace=True)

    # remove duplicates
    df.drop_duplicates(inplace=True)

    # replace blank values
    df["TotalCharges"] = df["TotalCharges"].replace(" ", pd.NA)

    # convert to numeric
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # remove missing values
    df.dropna(inplace=True)

    # split featurea and target
    X = df.drop(columns=["Churn"])
    y = df["Churn"]

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # merge back together
    train_df = pd.concat([X_train, y_train], axis=1)
    test_df = pd.concat([X_test, y_test], axis=1)

    # save datasets
    train_df.to_csv(TRAIN_FILE, index=False)
    test_df.to_csv(TEST_FILE, index=False)

    return train_df, test_df


if __name__ == "__main__":
    train_df, test_df = preprocess_data()

    print(train_df.shape)
    print(test_df.shape)
