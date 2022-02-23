from setuptools import setup, find_packages


setup(
    name='protein_viewer',
    version='0.1.0',
    install_requires=[
        "PySide6~=6.2.2.1",
        "biopython",
        "numpy~=1.22.1",
        "matplotlib~=3.5.1",
        "mayavi~=4.7.4",
        "setuptools~=60.5.0",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"}
)
