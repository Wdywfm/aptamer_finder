# Aptamer finder
## Installation
```
git clone https://github.com/Wdywfm/aptamer_finder.git
cd aptamer_finder
pip install .
```
## Usage
```
python src/protein_viewer/app.py
```
## Development methodology
This project follows trunk-based branching methodoly. It means, that it has only one branch - `main`.
To push new changes please create an additional branch e.g. `feature/cool_feature`:
```
git checkout -b feature/cool_feature          # create and checkout new branch
git add modified_file1.py modified_file2.py   # add desired files
git commit -m "Add new cool feature"          # commit changes
git push                                      # push branch to remote  
```
Navigate to https://github.com/Wdywfm/aptamer_finder/pulls and create a pull request.