import sys
import os
from pandas._config import config
sys.path.append(os.getcwd())
from data_download import load_config

import pandas as pd


def fillna(path2data):
    dataset = pd.read_csv(path2data)
    prepare_dataset = dataset.copy()
    for i, column in enumerate(dataset.columns):
        if i % 2 == 0:
            prepare_dataset[column] = prepare_dataset[column] - 1
        else:
            prepare_dataset[column] = prepare_dataset[column] - 2
    
    return prepare_dataset

if __name__ == "__main__":
    config = load_config("./src/configs/config.yaml")
    prepared_dataset = fillna(config["data_load"]["dataset_load"])
    prepared_dataset.to_csv(config["data_load"]["dataset_save"], index=False)
    