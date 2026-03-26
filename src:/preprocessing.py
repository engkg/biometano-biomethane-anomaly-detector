import pandas as pd
from sklearn.preprocessing import StandardScaler


FEATURE_COLUMNS = [
    "vazao_alimentacao",
    "producao_biogas",
    "temperatura",
    "pressao",
    "ch4",
]


def prepare_data(df: pd.DataFrame):
    df = df.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp").reset_index(drop=True)

    for col in FEATURE_COLUMNS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["timestamp"] + FEATURE_COLUMNS).reset_index(drop=True)

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[FEATURE_COLUMNS])

    return df, scaled_data