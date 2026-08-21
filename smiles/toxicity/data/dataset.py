from pathlib import Path

import pandas as pd


def loadds():

    pasta = Path(__file__).parent

    labels_df = pd.read_csv(
        pasta / "names_labels.csv", header=None, names=["name", "toxic"]
    )

    smiles_df = pd.read_csv(
        pasta / "names_smiles.csv", header=None, names=["name", "smiles"]
    )

    df = pd.merge(smiles_df, labels_df, on="name")

    return df
