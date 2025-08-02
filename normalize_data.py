import os
import pandas as pd

class NormalizeData:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir #read files inside bronze's folder
        self.output_dir = output_dir #save using parquet
        os.makedirs(output_dir, exist_ok=True) #ensures that the output folder exists


    def normalize_data(self):
       
        for file in os.listdir(self.input_dir):
            input_path = os.path.join(self.input_dir, file)
            name, ext = os.path.splitext(file) #separeted file name and extension
            output_path = os.path.join(self.output_dir, f'{name}.parquet')

            if ext.lower() == '.csv':
                df = pd.read_csv(input_path)
            elif ext.lower() == '.json':
                try:
                  df = pd.read_json(input_path)

                except ValueError:
                 df = pd.read_json(input_path, lines=True)
            else:
                print(f'error: file {file} ignored!')
                continue

            for col in df.columns:
                if df[col].apply(lambda x: isinstance(x, list)).any():
                    df[col] = df[col].apply(lambda x: str(x) if isinstance(x, list) else x)

            #convert columns type list to string to allows drop_duplicate
            df = df.drop_duplicates().reset_index(drop=True)

            #save file parquet format
            df.to_parquet(output_path, index=False)
            print(f"O arquivo {file} normalizado e salvo com {output_path}")

if __name__ == "__main__":
        normalize_data = NormalizeData(input_dir='01-bronze-raw', output_dir='02-silver-validated')
        normalize_data.normalize_data()