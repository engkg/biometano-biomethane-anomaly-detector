from pathlib import Path
import pandas as pd


REQUIRED_COLUMNS = [
    "timestamp",
    "vazao_alimentacao",
    "producao_biogas",
    "temperatura",
    "pressao",
    "ch4",
]


def load_data(file_path: str) -> pd.DataFrame:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    df = pd.read_csv(path)

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(
            f"Colunas obrigatórias ausentes no arquivo: {missing_columns}"
        )

    return df