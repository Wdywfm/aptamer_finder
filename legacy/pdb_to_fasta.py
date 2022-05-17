import sys
from Bio import SeqIO

PDBFile = "../data/1c9l.pdb"
with open(PDBFile, "r") as pdb_file:
    for record in SeqIO.parse(pdb_file, "pdb-atom"):
        print(">" + record.id)
        print(record.seq)
