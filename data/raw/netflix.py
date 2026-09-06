import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
pasta_entrada = BASE / 'data' / 'raw'
pasta_saida = BASE / 'data' / 'ready'
arquivos = sorted(pasta_entrada.glob('*.xlsx'))

dfs = []

if not arquivos:
    print('Nenhum arquivo compátivel encontrado')
else:
    for arquivo in arquivos:

        try:
            df_temp = pd.read_excel(arquivo)
            file_name = arquivo.name
            if 'brasil' in file_name.lower():
                df_temp['País'] = 'Br'
            elif 'france' in file_name.lower():
                df_temp['País'] = 'Fr'

            df_temp.columns = df_temp.columns.str.strip()
            df_temp['Campanha'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')
            df_temp['Campanha'] = df_temp['Campanha'].str.upper().str.capitalize()
            df_temp.rename(columns={'sale_date': 'Data de Venda',
                                    'Customer': 'Assinante',
                                    'Contracted Plan': 'Plano Contratado',
                                    'Amount': 'Valor',
                                    'utm_link': 'URL',
                                    'Age': 'Idade'}, inplace=True)
            dfs.append(df_temp)

        except Exception as e:
            print(f'Erro ao ler o arquivo {arquivo}: {e}')
if dfs:
    resultado = pd.concat(dfs, ignore_index = True)
    pasta_saida.mkdir(parents=True, exist_ok=True)
    caminho_excel = pasta_saida / 'clean.xlsx'
    caminho_csv = pasta_saida / 'clean.csv'

    with pd.ExcelWriter(caminho_excel, engine='xlsxwriter') as writer:
        resultado.to_excel(writer, index=False)

    resultado.to_csv(caminho_csv, index=False)
    print(f'{len(resultado)} linhas salvas em {caminho_excel} e {caminho_csv}')
else:
    print('Nenhum dado para ser salvo')
