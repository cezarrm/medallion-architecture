import boto3
import os

bucket_name = 'etl-cezar-projeto-01'
s3 = boto3.client('s3')

def upload_folder(local_folder, s3_prefix):
    for filename in os.listdir(local_folder):
        local_path = os.path.join(local_folder, filename) #cria variavel com caminho local dos arquivo e concatena com arquivo
        if os.path.isfile(local_path): #se for um arquivo executa
            s3_key = f"{s3_prefix}/{filename}" 
            s3.upload_file(local_path, bucket_name, s3_key)
            print(f"Arquivo {filename} enviado para s3://{bucket_name}/{s3_key}")

if __name__ == "__main__":
    #upload script
    upload_folder('.', 'scripts') #pega script.py e normalize_data.py

    #upload camada bronze
    upload_folder('01-bronze-raw', '01-bronze-raw')

    #upload camada silver
    upload_folder('02-silver-validated', '02-silver-validated')
