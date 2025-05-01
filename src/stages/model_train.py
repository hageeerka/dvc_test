import sys
import os
from pandas._config import config
sys.path.append(os.getcwd())
from data_download import load_config

import pickle

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from yaml import load, Loader
from dvclive import Live

def train(config):
    np.random.seed(config["train_config"]["seed"])

    features_path = config["path"]["features_path"]
    target_path = config["path"]["target_path"]

    dataset = pd.read_csv(features_path)
    target = pd.read_csv(target_path)

    train_index, validation_index = train_test_split(dataset.index, 
                                                     test_size=config["train_config"]["validation_size"])

    train_index, test_index = train_test_split(train_index, 
                                               test_size=config["train_config"]["test_size"])

    model = LinearRegression()
    model.fit(dataset.loc[train_index], target.loc[train_index])

    train_MSE = mean_squared_error(target.loc[test_index], 
                                   model.predict(dataset.loc[test_index]))

    test_MSE = mean_squared_error(target.loc[train_index], 
                                  model.predict(dataset.loc[train_index]))

    validation_MSE = mean_squared_error(target.loc[validation_index], 
                                        model.predict(dataset.loc[validation_index]))
    
    models_path = config["models_save"]["path"]

    with open(models_path, "wb") as mod:
        mod.write(pickle.dumps(model))
    
    with Live(save_dvc_exp=True) as live:
        live.log_artifact(models_path)
        live.log_metric("train_MSE", train_MSE)
        live.log_metric("test_MSE", test_MSE)
        live.log_metric("validation_MSE", validation_MSE)

if __name__ == "__main__":
    config = load_config("./src/configs/config.yaml")
    train(config)

    