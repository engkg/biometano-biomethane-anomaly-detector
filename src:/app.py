from pathlib import Path

from io_utils import load_data
from preprocessing import prepare_data
from modeling import run_model
from charts import save_chart


def main():
    input_file = "data/operacao_exemplo.csv"
    output_table = "outputs/resultado_monitoramento.csv"
    output_chart = "outputs/grafico_monitoramento.png"

    Path("outputs").mkdir(exist_ok=True)

    print("Lendo arquivo de entrada...")
    df = load_data(input_file)

    print("Preparando dados...")
    prepared_df, scaled_data = prepare_data(df)

    print("Executando modelo...")
    result_df = run_model(prepared_df, scaled_data, contamination=0.15)

    print("Salvando resultados...")
    result_df.to_csv(output_table, index=False)

    print("Gerando gráfico...")
    save_chart(result_df, output_chart)

    print("Concluído.")
    print(f"Tabela gerada em: {output_table}")
    print(f"Gráfico gerado em: {output_chart}")


if __name__ == "__main__":
    main()