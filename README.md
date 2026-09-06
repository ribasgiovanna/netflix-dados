# 🎬 Pipeline de Dados — Marketing Netflix (estudo de ETL)

Pipeline em **Python + pandas** que consolida várias planilhas de vendas por país,
extrai a campanha de marketing da URL de rastreio (UTM) e entrega um único arquivo
limpo em **CSV e Excel**.

> Dados **fictícios**, criados para praticar ETL. Nenhuma informação real de clientes.

## 🔄 Entrada → Processamento → Saída

**Entrada:** todas as planilhas em `data/raw/*.xlsx` (uma por país / mês)

1. Lê cada planilha e identifica o país pelo nome do arquivo
   (`brasil` → `Br`, `france` → `Fr`)
2. Limpa os nomes das colunas
3. Extrai o valor de `utm_campaign=` da URL de rastreio para uma coluna `Campanha`
4. Renomeia as colunas para português
   (`sale_date` → `Data de Venda`, `Amount` → `Valor`, …)
5. Junta tudo em uma tabela só

**Saída:** `data/ready/clean.csv` e `data/ready/clean.xlsx`

## 🛠️ Tecnologias

- Python 3
- pandas
- XlsxWriter (escrita do `.xlsx`)

## 📁 Estrutura

```
.
└── data/
    ├── raw/
    │   ├── netflix.py                    # pipeline
    │   ├── netflix_202401_brasil.xlsx    # dados de exemplo
    │   └── netflix_202402_france.xlsx
    └── ready/
        ├── clean.csv                     # resultado consolidado
        └── clean.xlsx
```

## ▶️ Como executar

```bash
pip install pandas xlsxwriter openpyxl
python data/raw/netflix.py
```

Execute a partir da raiz do projeto. Para acrescentar fontes, coloque novas planilhas
em `data/raw/` seguindo o padrão de nome `..._pais.xlsx`.

## 👤 Autoria

Desenvolvido por **Giovanna Ribas dos Reis** — projeto individual.

## 🧭 Próximos passos possíveis

- Mapear o país por um dicionário, aceitando novos países sem alterar o código
- Validar as colunas esperadas antes de processar

## 🤖 Transparência

O código deste projeto é de autoria própria, sem geração por IA.
