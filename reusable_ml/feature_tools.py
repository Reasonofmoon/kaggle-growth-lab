import pandas as pd


def add_missing_indicators(df, columns):
    result = df.copy()
    for column in columns:
        result[f"{column}_is_missing"] = result[column].isna().astype("int8")
    return result


def align_train_test_columns(train, test):
    train_aligned, test_aligned = train.align(test, join="left", axis=1, fill_value=0)
    return pd.DataFrame(train_aligned), pd.DataFrame(test_aligned)
