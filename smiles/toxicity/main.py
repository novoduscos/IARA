from data.dataset import loadds
from fingerprints.maccs import smiles_to_maccs
from numpy import array

df = loadds()

maccs = []
vector = []

invalid_ind = []
invalid_smile = []

for index, row in df[["smiles", "toxic"]].iterrows():
    smiles = row["smiles"]
    toxic = row["toxic"]

    fp = smiles_to_maccs(smiles)
    if fp is not None:
        maccs.append(fp)
        vector.append(toxic)
    else:
        invalid_ind.append(index)
        invalid_smile.append(smiles)
