"""
Реализация алгоритма поиска участка с наиболее сильными связями
"""

import numpy as np
import matplotlib.pyplot as plt
from Bio.PDB import PDBParser, PPBuilder


class AlphaPoint(object):
    def __init__(self, vector, resseq, chainName):
        """Constructor"""
        self.vector = vector
        self.resseq = resseq
        self.chainName = chainName

    def __eq__(self, other):
        if not self.__class__ == other.__class__:
            return False

        distance = np.linalg.norm(self.vector - other.vector)
        return distance == 0 and self.resseq == other.resseq and self.chainName == other.chainName

    def __hash__(self):
        return self.resseq


# ----------

# ----------
# Support Functions

def show_points(alpha_Points):
    x = []
    y = []
    z = []
    c = []

    for point in alpha_Points:
        x.append(point.vector[0])
        y.append(point.vector[1])
        z.append(point.vector[2])
        c.append(colors[point.chainName])

    return [x, y, z, c]


# ----------

# Preferences
pdb_file = '1j1d_2.pdb'
T = 7  # Range
searching_keys = [
    # 'A',
    # 'B',
    'C'
    # 'D',
    # 'E',
    # 'F'
]
colors = {
    'A': 'm',
    'B': 'g',
    'C': 'b',
    'D': 'r',
    'E': 'y',
    'F': 'c'
}

# Map of distances peptides in chains
chaines_map_distances = dict()
chain_map = dict()

# Initialisation
parser = PDBParser()
structure = parser.get_structure('structure_name', pdb_file)

# получаем все цепочки
chains = dict()
for model in structure:
    for chain in model:
        chains[chain.id] = chain

#######
# получаем координаты alpha-углеродов
ppb = PPBuilder()

# Mapping vectors distances
for chain_id_a in chains:
    # Build polypeptides
    pp_a = ppb.build_peptides(chains[chain_id_a])
    chaines_map_distances[chain_id_a] = dict()
    chain_map[chain_id_a] = []

    for chain_id_b in chains:
        if chain_id_a == chain_id_b:
            continue

        # Build polypeptides
        pp_b = ppb.build_peptides(chains[chain_id_b])

        for el_a in pp_a:
            alpha_carbons_a = el_a.get_ca_list()

            for el_b in pp_b:
                alpha_carbons_b = el_b.get_ca_list()

                for atom_a in alpha_carbons_a:
                    resseq_a = atom_a.get_parent().get_full_id()[3][1]
                    vector_a = atom_a.get_vector()
                    chain_map[chain_id_a].append((AlphaPoint(vector_a, resseq_a, chain_id_a)))

                    for atom_b in alpha_carbons_b:
                        # atom_b.get_parent() = residue
                        resseq_b = atom_b.get_parent().get_full_id()[3][1]
                        vector_b = atom_b.get_vector()
                        distance = np.linalg.norm(vector_a - vector_b)

                        if not distance in chaines_map_distances[chain_id_a].keys():
                            chaines_map_distances[chain_id_a][distance] = []

                        chaines_map_distances[chain_id_a][distance].append(
                            (AlphaPoint(vector_a, resseq_a, chain_id_a), AlphaPoint(vector_b, resseq_b, chain_id_b)))

# Search chins and printig
alpha_Points = set()

for key in searching_keys:
    if not key in chaines_map_distances.keys():
        continue

    range_chaines_map = chaines_map_distances[key]

    for (key, value) in range_chaines_map.items():
        if not key < T:
            continue

        for deps in value:
            vector_a, vector_b = deps

            # Focused on searched chains
            # alpha_Points.add(vector_a)

            # Show contact chains
            if not vector_b.chainName in searching_keys:
                alpha_Points.add(vector_b)

fig = plt.figure()
ax = plt.axes(projection='3d')

contactPoints = show_points(alpha_Points)
ax.scatter3D(contactPoints[0], contactPoints[1], contactPoints[2], color=contactPoints[3], s=2)

for key in searching_keys:
    result = show_points(chain_map[key])
    ax.scatter3D(result[0], result[1], result[2], color=result[3], s=2)

plt.show()
