import requests
import pandas as pd


def get_data(cep):
    #receive a cep as parameter and replace in the http request
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(endpoint)  # Request API
        cep_info = response.json()
        return cep_info

    except requests.exceptions.RequestException as e:
        print(f"error during API request: {e} in {cep}")



users_path = '01-bronze-raw/users.csv'
users_df = pd.read_csv(users_path)

cep_lists = users_df['cep'].tolist() #return just the first 5 users and transform "column-object" on list

cep_info_list = []


#iterate in the cep_lists and request in the get_data and append in cep_info_list
for cep in cep_lists: 
    cep_info = get_data(cep)
    print(cep_info)
    if "erro" in cep_info:
        continue
    cep_info_list.append(cep_info)

cep_info_df = pd.DataFrame(cep_info_list)
cep_info_df.to_csv("01-bronze-raw/cep_info.csv", index=False)    