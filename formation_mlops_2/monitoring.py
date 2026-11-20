import pandas as pd


def monitor(latest_predictions: pd.DataFrame) -> pd.DataFrame:
    # Start filling function
    means = latest_predictions.groupby('predictions_time')['predictions'].mean()  # Series, index = predictions_time
    monitoring_df = pd.DataFrame({
        'predictions_time': means.index,
        'predictions': means.values,
    })
    # End filling function
    return monitoring_df
