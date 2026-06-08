from math import sqrt

from sklearn.metrics import mean_absolute_error, mean_squared_error, roc_auc_score


def regression_scores(y_true, y_pred):
    return {
        "mae": mean_absolute_error(y_true, y_pred),
        "rmse": sqrt(mean_squared_error(y_true, y_pred)),
    }


def binary_classification_scores(y_true, y_pred_proba):
    return {
        "roc_auc": roc_auc_score(y_true, y_pred_proba),
    }
