import os
import sys

from pandas._config import config
sys.path.append(os.getcwd())

import yaml
from sklearn import datasets
import pandas as pd

def load_config(config_path):
    with open(config_path) as conf_file:
        config = yaml.safe_load(conf_file)
    return config

def load_dataset(config):
    dataset = datasets.load_diabetes()
    features = pd.DataFrame(data=dataset.data, 
                            columns=["feat%s" % x for x in range(dataset.data.shape[1])])
    target = pd.DataFrame(data=dataset.target, columns=["target"])

    features_path = config["path"]["features_path"]
    target_path = config["path"]["target_path"]


    features.to_csv(features_path)
    target.to_csv(target_path)

if __name__ == "__main__":  
    config = load_config("./src/configs/config.yaml")
    load_dataset(config)