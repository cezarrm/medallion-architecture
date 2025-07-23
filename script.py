import requests
import pandas as pd


def get_data(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(endpoint)  # Request API
        cep_info = response.json()
        return cep_info

    except requests.exceptions.RequestException as e:
        print(f"error during API request: {e}")



users_path = '01-bronze-raw/users.csv'
users_df = pd.read_csv(users_path)

cep_lists = users_df['cep'].tolist() #retorna só os 5 primeiros usuários e transforma coluna objeto em lista

for cep in cep_lists: 
    cep_info = get_data(cep)
    print(cep_info)