import os

from sklearn import datasets

import pandas as pd


if __name__ == "__main__":
    dataset = datasets.load_diabetes()
    features = pd.DataFrame(data=dataset.data, 
                            columns=["feat%s" % x for x in range(dataset.data.shape[1])])
    target = pd.DataFrame(data=dataset.target, columns=["target"])

    output_dir = r"C:\Users\go130\dvc_example\data\initial_data"
    os.makedirs(output_dir, exist_ok=True)  # создаст папку, если её нет

    features.to_csv(os.path.join(output_dir, "initial_data.csv"), index=False)
    target.to_csv(os.path.join(output_dir, "target.csv"), index=False)
