# Utility Methods

```python 
isRNA(files)
```
Utility method to determine whether or not a specified molecule object contains residues
that classify molecule as an RNA molecular structure.

__Parameters__:

* mol (Molecule): Molecule object reference

__Return__:

* rna (bool): True if molecule object contains RNA residues in polymeric chain, false otherwise. 

See module: `predictor.py`


```python
getFullSequence(molecule)
```
Utility method that gets full sequence name contents of molecule object reference.

__Parameters__:

* molecule (Molecule): Molecule object reference

__Return__:

* seqList (list): A list of polymer and residue names and numbers if contents exists within molecule reference. Empty list otherwise.

See module: `rnapred.py` 
