# Netflix Data Pipeline - ETL study

A Python and pandas pipeline that consolidates several sales spreadsheets by country,
extracts the marketing campaign from the tracking (UTM) URL, and produces a single
clean file in CSV and Excel.

Fictional data, created to practice ETL. No real customer information.

## Input -> Processing -> Output

**Input:** every spreadsheet in `data/raw/*.xlsx` (one per country / month)

1. Reads each spreadsheet and identifies the country from the file name
   (`brasil` -> `Br`, `france` -> `Fr`)
2. Cleans the column names
3. Extracts the `utm_campaign=` value from the tracking URL into a `Campanha` column
4. Renames the columns to Portuguese
5. Concatenates everything into a single table

**Output:** `data/ready/clean.csv` and `data/ready/clean.xlsx`

## Tech

- Python 3
- pandas
- XlsxWriter (`.xlsx` writing)

## Structure

```
.
└── data/
    ├── raw/
    │   ├── netflix.py                    # pipeline
    │   ├── netflix_202401_brasil.xlsx    # sample data
    │   └── netflix_202402_france.xlsx
    └── ready/
        ├── clean.csv                     # consolidated result
        └── clean.xlsx
```

## Running

```bash
pip install pandas xlsxwriter openpyxl
python data/raw/netflix.py
```

Paths are resolved relative to the script itself, so it runs from any directory. To add
sources, drop new spreadsheets into `data/raw/` following the `..._country.xlsx` naming.

## Authorship

Written by Giovanna Ribas dos Reis - individual project.

## Next steps

- Map the country through a dictionary, accepting new countries without code changes
- Validate the expected columns before processing

## Transparency

The code in this project is my own work, not AI-generated.
