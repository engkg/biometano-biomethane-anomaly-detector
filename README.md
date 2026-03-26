# Monitoramento de dados operacionais em planta de biometano

Projeto em Python para leitura, tratamento e análise de dados operacionais.

O objetivo é identificar pontos de operação fora do padrão em séries de processo.

---

## Contexto

Plantas industriais operam continuamente e geram grande volume de dados. Nem sempre desvios operacionais são percebidos rapidamente, principalmente quando ocorrem de forma gradual. Este projeto propõe uma abordagem simples para inicialmente destacar comportamentos fora do padrão.

---

## O que o projeto faz

- lê um arquivo CSV com dados operacionais  
- trata e organiza os dados  
- aplica um modelo para identificar desvios  
- gera uma tabela com os resultados  
- gera um gráfico com os pontos fora do padrão  

---

## Estrutura do projeto

biometano-anomaly-detector/data (operacao_exemplo.csv); outputs/; src/ (app.py, io_utils.py, preprocessing.py, modeling.py, charts.py); README.md (requirements.txt; .gitignore)

---

## Estrutura do arquivo de entrada

O arquivo CSV inicialmente deve conter as seguintes colunas:

- timestamp  
- vazao_alimentacao  
- producao_biogas  
- temperatura  
- pressao  
- ch4  

Exemplo:

timestamp,vazao_alimentacao,producao_biogas,temperatura,pressao,ch4
2026-01-01 00:00,120,850,37.1,1.20,58.2

Outros dados podem ser adicionados para deixar o modelo mais robusto.

---

## Como executar

pip install -r requirements.txt  
python src/app.py  

---

## Saídas geradas

Após a execução:

- outputs/resultado_monitoramento.csv  
- outputs/grafico_monitoramento.png  

---

## Interpretação

A coluna anomalia indica:

0 → comportamento dentro do padrão  
1 → ponto fora do padrão  

---

## Limitações

- o modelo não identifica a causa do desvio  
- depende da qualidade dos dados  
- não substitui análise de processo. é um complemento.  

---

## Possíveis evoluções

- geração de relatório automático  
- inclusão de novas variáveis  
- integração com dados reais  

---

## Observação final

O projeto foi estruturado para funcionar com dados simples em CSV, sem depender de sistemas industriais ou ferramentas proprietárias.

A ideia é permitir análise rápida e reprodutível.
