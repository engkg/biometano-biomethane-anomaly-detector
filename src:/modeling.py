import pandas as pd
from sklearn.ensemble import IsolationForest


def run_model(df: pd.DataFrame, scaled_data, contamination: float = 0.15) -> pd.DataFrame:
    model = IsolationForest(
        n_estimators=100,
        contamination=contamination,
        random_state=42
    )

    model.fit(scaled_data)

    labels = model.predict(scaled_data)
    scores = model.decision_function(scaled_data)

    result = df.copy()
    result["model_flag"] = labels
    result["score"] = scores
    result["anomalia"] = result["model_flag"].apply(lambda x: 1 if x == -1 else 0)

    return result