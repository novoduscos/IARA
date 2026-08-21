import numpy as np
from rdkit import Chem, DataStructs
from rdkit.Chem import MACCSkeys


def smiles_to_maccs(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    fp = MACCSkeys.GenMACCSKeys(mol)

    ar = np.zeros((fp.GetNumBits(),), dtype=np.int8)

    DataStructs.ConvertToNumpyArray(fp, ar)

    return ar
