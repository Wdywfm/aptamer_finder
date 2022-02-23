"""
Поиск полипептидных связей с помощью CA - CA связей
"""

import numpy as np
from mayavi import mlab
from Bio.PDB import PDBParser, CaPPBuilder

pdb_file = '1j1d_2.pdb'

parser = PDBParser()
structure = parser.get_structure('structure_name', pdb_file)

# получаем все цепочки
chains = dict()
for model in structure:
    for chain in model:
        chains[chain.id] = chain

# получаем координаты alpha-углеродов
ppb = CaPPBuilder()

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

colors = [
    (0.964, 0.211, 0.192),
    (0.192, 0.376, 0.964),
    (0.192, 0.964, 0.713),
    (0.964, 0.917, 0.192),
    (0.964, 0.592, 0.192),
    (0.807, 0.274, 0.764)
]

mlab.figure(1, bgcolor=(1, 1, 1))
mlab.clf()

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
        mlab.points3d(el[:, 0], el[:, 1], el[:, 2], scale_factor=1, scale_mode='none', color=colors[idx], resolution=20)
        mlab.plot3d(el[:, 0], el[:, 1], el[:, 2], color=colors[idx], line_width=10)
mlab.show()
