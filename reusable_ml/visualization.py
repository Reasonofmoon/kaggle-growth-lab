import matplotlib.pyplot as plt
import seaborn as sns


def plot_missing_values(df, top_n=30):
    missing = df.isna().mean().sort_values(ascending=False).head(top_n)
    missing = missing[missing > 0]

    if missing.empty:
        return None

    fig, ax = plt.subplots(figsize=(10, max(4, len(missing) * 0.35)))
    sns.barplot(x=missing.values, y=missing.index, ax=ax)
    ax.set_xlabel("Missing ratio")
    ax.set_ylabel("Feature")
    ax.set_title("Missing values by feature")
    return ax
