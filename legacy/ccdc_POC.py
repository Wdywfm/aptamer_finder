from ccdc.protein import Protein
from ccdc.molecule import Molecule
from ccdc.io import MoleculeReader
import numpy as np


if __name__ == "__main__":
    molecule = MoleculeReader("../data/1keb.pdb")[0]
    criterion = Molecule.HBondCriterion()
    hbonds = molecule.hbonds(hbond_criterion=criterion)
    for bond in hbonds:
        atom_1, atom_2 = bond.atoms
        print(atom_1.residue_label, atom_2.residue_label)
        atom_1_coords, atom_2_coords = np.array(atom_1.coordinates), np.array(atom_2.coordinates)
        print(
            np.sqrt(
                (atom_1_coords[0] - atom_2_coords[0]) ** 2
                + (atom_1_coords[1] - atom_2_coords[1]) ** 2
                + (atom_1_coords[2] - atom_2_coords[2]) ** 2
            )
        )
        print(f"Angle: {bond.angle}, Distance: {bond.da_distance}, Length: {bond.length}, Strength: {bond.strength}")
