import os

from dotenv import load_dotenv
import pandas as pd

output_dir = r"C:\Users\go130\dvc_example\data"
prepared_data_dir = os.path.join(output_dir, "prepared_data")
initial_data_file = os.path.join(output_dir, "initial_data", "initial_data.csv")
prepared_data_file = os.path.join(prepared_data_dir, "prepared_data.csv")

def fillna(dataset: pd.DataFrame) -> pd.DataFrame:

    prepare_dataset = dataset.copy()
    for i, column in enumerate(dataset.columns):
        if i % 2 == 0:
            prepare_dataset[column] = prepare_dataset[column] - 1
        else:
            prepare_dataset[column] = prepare_dataset[column] - 2
    
    return prepare_dataset

if __name__ == "__main__":
    dataset = pd.read_csv(initial_data_file)
    prepared_dataset = fillna(dataset=dataset)
    prepared_dataset.to_csv(prepared_data_file, index=False)