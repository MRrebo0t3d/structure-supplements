<h1 id="refine.refine">refine</h1>

```python
refine(self)
```

<h2 id="refine.refine.writeAngles">writeAngles</h2>

```python
refine.writeAngles(self, fileName)
```

__Parameters:__


fileName (string): name of file with angles/dihedral constraints

__Return:__


None

See also: `writeDihedrals(fileName)`

<h2 id="refine.refine.readAngles">readAngles</h2>

```python
refine.readAngles(self, fileName)
```

__Parameters:__


fileName (string): name of file with angles/dihedral constraints

__Return:__


None

See also: `readDihedrals(fileName)`

<h2 id="refine.refine.setAngles">setAngles</h2>

```python
refine.setAngles(self, ranfact, mode)
```

__Parameters:__


* ranfact (???) : ???
* mode (bool) : Describes whether or not to use random initial angles.

See also: `putInitialAngles(...)` in Dihedrals.java

<h2 id="refine.refine.randomizeAngles">randomizeAngles</h2>

```python
refine.randomizeAngles(self)
```
Generates random angles

See also: `randomizeAngles(...)` in Dihedrals.java

<h2 id="refine.refine.updateAt">updateAt</h2>

```python
refine.updateAt(self, n)
```

__Parameters:__


n (int) : ???

See also: `updateAt(...)` in Dihedrals.java

<h2 id="refine.refine.setForces">setForces</h2>

```python
refine.setForces(self, robson=None, repel=None, elec=None, dis=None, tors=None, dih=None, irp=None, shift=None, bondWt=None)
```

__Parameters:__


* robson (???) : ???
* repel (???) : ???
* elec (???) : ???
* dis (???) : ???
* tors (???) : ???
* dih (???) : ???
* shift (???) : ???
* bondWt (???) : ???

<h2 id="refine.refine.getForces">getForces</h2>

```python
refine.getForces(self)
```

__Return:__


output (string) : string that contains values of the calculated forces

<h2 id="refine.refine.printPars">printPars</h2>

```python
refine.printPars(self)
```
prints out parameters as a tuple....?
<h2 id="refine.refine.getEntityTreeStartAtom">getEntityTreeStartAtom</h2>

```python
refine.getEntityTreeStartAtom(self, entity)
```
getEntityTreeStartAtom returns an atom that would be picked up
by AngleTreeGenerator if no atom is specified.

<h2 id="refine.refine.getAtom">getAtom</h2>

```python
refine.getAtom(self, atomTuple)
```
Gets atom from a tuple that contains entity and atom name.

__Paramters:__


atomTuple (tuple) : ...

<h2 id="refine.refine.loadFromYaml">loadFromYaml</h2>

```python
refine.loadFromYaml(self, data, seed, pdbFile='')
```
Reading in all the structures
<h2 id="refine.refine.addSuiteAngles">addSuiteAngles</h2>

```python
refine.addSuiteAngles(self, fileName)
```

__Parameters:__


fileName (string) : ....

<h2 id="refine.refine.setupTree">setupTree</h2>

```python
refine.setupTree(self, treeDict)
```
Creates the tree path and setups the coordinates of the molecule from all the entities

Keyword arguments:
treeDict -- A dictionary that might contain start, end, and measure

Dictionary Keys:
start   -- Full name of the first atom in building the tree
end     -- Full name of the last atom in building the tree

<h2 id="refine.refine.predictShifts">predictShifts</h2>

```python
refine.predictShifts(self)
```
Predict chemical shifts ...

__Returns:__


shifts (list) : ....

<h2 id="refine.refine.setShifts">setShifts</h2>

```python
refine.setShifts(self, shiftFile)
```
Reads a chemical shifts from file and returns array of shifts

__Parameters:__


shiftFile (string) : chemical shifts file

__Returns:__


shifts (list) : ...

<h2 id="refine.refine.setup">setup</h2>

```python
refine.setup(self, homeDir, seed, writeTrajectory=False, usePseudo=False, useShifts=False)
```
Set up parameters and methods to run program and generate structure.
__Parameters:__


homeDir (string) : ....
seed (int) : ...
writeTrajectory (bool) : ...
usePseudo (bool) : ....
useShifts (bool) : ....

<h2 id="refine.refine.addRingClosures">addRingClosures</h2>

```python
refine.addRingClosures(self)
```
Close ring structure using distance constraint on specified atoms within ring.
<h2 id="refine.refine.polish">polish</h2>

```python
refine.polish(self, steps, usePseudo=False, stage1={})
```
Calls the functions relevant for generation of structures...?
__Parameters:__


* steps (int) : ???
* usePseudo (bool) : ???
* stage1 (dict) : ???


<h2 id="refine.refine.output">output</h2>

```python
refine.output(self)
```
Prints out energy and execution time to the commandline.
Handles parameters for various methods if output directory has been generated.

<h2 id="refine.refine.dumpDis">dumpDis</h2>

```python
refine.dumpDis(self, fileName, delta=0.5, atomPat='*.H*', maxDis=4.5, prob=1.1, fixLower=0.0)
```
Writes a dump file containing distance violations based on input distance
constraints and actual distance between atoms.

__Parameters:__


* fileName (string) : name of the output dump file
* delta (float) : ???
* atomPat (string) : ???
* maxDis (float) : ???
* prob (float) : ???
* fixLower (float) : ???

<h2 id="refine.refine.dumpAngles">dumpAngles</h2>

```python
refine.dumpAngles(self, fileName, delta=10)
```
Writes a dump file containing dihedral violations based on input dihedral constraints and actual dihedral.
__Parameters:__


* fileName (string) : name of angles file
* delta (int) : ???


<h2 id="refine.refine.setPeptideDihedrals">setPeptideDihedrals</h2>

```python
refine.setPeptideDihedrals(self, phi, psi)
```
Using specified phi and psi angles to calculate dihedral angle and generate coordinates.
__Parameters:__


phi (float) : rotation angles around bonds b/t N - Calpha
psi (float) : rotation angles around bonds b/t Calpha - C

__Returns:__


None


