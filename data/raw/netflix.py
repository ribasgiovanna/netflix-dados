import pandas as pd
import os 
import glob  

caminho_pasta = r'data\raw'
arquivos = glob.glob(os.path.join(caminho_pasta, "*.xlsx"))

dfs = []

if not arquivos:
    print('Nenhum arquivo compátivel encontrado')
else:
    for arquivos in arquivos:
        
        try:
            df_temp = pd.read_excel(arquivos)
            file_name = os.path.basename(arquivos)
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
            print(df_temp)

        except Exception as e:
            print(f'Erro ao ler o arquivo {arquivos}: {e}')
if dfs:
    resultado = pd.concat(dfs, ignore_index = True)
    pasta_saida = os.path.join('data', 'ready')
    caminho_excel = os.path.join(pasta_saida, 'clean.xlsx')

    caminho_csv = os.path.join(pasta_saida, 'clean.csv')
    writer = pd.ExcelWriter(caminho_excel, engine = 'xlsxwriter')
    resultado.to_excel(writer, index = False)
    writer._save()

    resultado.to_csv(caminho_csv, index = False)
else:
    print('Nenhum dado para ser salvo')
     