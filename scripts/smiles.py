import pandas as pd
from rdkit import Chem
import os


def main():
    df = pd.read_csv("glycans/ids.csv", dtype=str)
    smiles = []
    for index, row in df.iterrows():
        if not os.path.exists("./glycans/" + row["Code"] + ".pdb"):
            smiles.append("")
            continue

        mol = Chem.MolFromPDBFile("./glycans/" + row["Code"] + ".pdb")
        if "one" in str(type(mol)):
            smiles.append("")
            continue

        # print(Chem.MolToSmiles(mol))
        Chem.AssignAtomChiralTagsFromStructure(mol)
        # Chem.AssignChiralTypesFromBondDirs(mol)
        smiles.append(Chem.MolToSmiles(mol, isomericSmiles=True, kekuleSmiles=True))
        # print(Chem.MolToSmiles(mol, isomericSmiles=True, kekuleSmiles=True), end="\n\n")
    df["Smiles"] = smiles
    df.to_csv("smiles.csv", index=False)


if __name__ == '__main__':
    main()

