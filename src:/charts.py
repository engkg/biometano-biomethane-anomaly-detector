from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def save_chart(df: pd.DataFrame, output_file: str) -> None:
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    normal_data = df[df["anomalia"] == 0]
    anomaly_data = df[df["anomalia"] == 1]

    plt.figure(figsize=(12, 6))
    plt.plot(
        normal_data["timestamp"],
        normal_data["producao_biogas"],
        marker="o",
        label="Operação"
    )
    plt.scatter(
        anomaly_data["timestamp"],
        anomaly_data["producao_biogas"],
        marker="x",
        s=100,
        label="Ponto fora do padrão"
    )

    plt.title("Monitoramento de produção de biogás")
    plt.xlabel("Tempo")
    plt.ylabel("Produção de biogás")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()