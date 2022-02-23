"""
Реализация алгоритмоа поиска полипептидной последовательности
"""
import numpy as np
import matplotlib.pyplot as plt
from Bio.PDB import PPBuilder, PDBParser

pdb_file = '1j1d_2.pdb'

parser = PDBParser()
structure = parser.get_structure('structure_name', pdb_file)

# получаем все цепочки
chains = dict()
for model in structure:
    for chain in model:
        chains[chain.id] = chain

# получаем координаты alpha-углеродов
ppb = PPBuilder()
v = dict()
for chain_id in chains:
    vectors = []
    pp = ppb.build_peptides(chains[chain_id])
    for el in pp:
        alpha_carbons = el.get_ca_list()
        for atom in alpha_carbons:
            residue = atom.get_parent()
            residue_id = residue.get_full_id()
            resseq = residue_id[3][1]
            vectors.append([*atom.get_vector(), resseq])
    vectors = np.array(vectors)
    v[chain_id] = vectors

colors = ['m', 'g', 'b', 'r', 'c', 'k']

fig = plt.figure()
ax = plt.axes(projection='3d')

for idx, chain_id in enumerate(chains):
    vect = v[chain_id]
    res = []
    prev = vect[0, 3]
    cur = [vect[0, :]]
    for el in vect[1:, :]:
        if el[3] - prev > 1:
            cur = np.array(cur)
            res.append(cur)
            cur = [el]
        else:
            cur.append(el)
        prev = el[3]
    cur = np.array(cur)
    res.append(cur)

    for el in res:
        ax.plot3D(el[:, 0], el[:, 1], el[:, 2], color=colors[idx], linewidth=0.5)
        ax.scatter3D(vect[:, 0], vect[:, 1], vect[:, 2], color=colors[idx], s=3)
plt.show()
