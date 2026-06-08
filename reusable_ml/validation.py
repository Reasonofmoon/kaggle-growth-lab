from sklearn.model_selection import KFold, StratifiedKFold


def make_kfold(n_splits=5, shuffle=True, random_state=42):
    return KFold(
        n_splits=n_splits,
        shuffle=shuffle,
        random_state=random_state,
    )


def make_stratified_kfold(n_splits=5, shuffle=True, random_state=42):
    return StratifiedKFold(
        n_splits=n_splits,
        shuffle=shuffle,
        random_state=random_state,
    )
