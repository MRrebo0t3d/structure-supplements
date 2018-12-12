<h1 id="refine_wo_imp.refine">refine</h1>

```python
refine(self)
```

<h2 id="refine_wo_imp.refine.writeAngles">writeAngles</h2>

```python
refine.writeAngles(self, fileName)
```
Utility method used to redirect dihedral constraint file name onto java method.
Ultimately writes dihedral angles TO a specified file.

__Parameters:__


* fileName (string): Output file name that'll contain dihedral angle constraints.

See also: `writeDihedrals(...)` in Dihedral.java

<h2 id="refine_wo_imp.refine.readAngles">readAngles</h2>

```python
refine.readAngles(self, fileName)
```
Utility method used to redirect dihedral constraint file name onto java method.
Ultimately reads dihedral angles FROM a specified file.

__Parameters:__


* fileName (string): Input file name to read angle constraints from.

See also: `readDihedrals(...)` in Dihedral.java

<h2 id="refine_wo_imp.refine.setAngles">setAngles</h2>

```python
refine.setAngles(self, mode)
```
Utility setter method used to redirect boolean that determines whether or not
to ...(?) when initializing an array list of angles.

__Parameters:__


* mode (bool) : Describes whether or not to use random initial angles.

See also: `putInitialAngles(...)` in Dihedrals.java

<h2 id="refine_wo_imp.refine.randomizeAngles">randomizeAngles</h2>

```python
refine.randomizeAngles(self)
```
Utility method used to generate random angles.

See also: `randomizeAngles(...)` in Dihedrals.java

<h2 id="refine_wo_imp.refine.updateAt">updateAt</h2>

```python
refine.updateAt(self, n)
```
Utility method that describes how often to update the atom bound contact list used
during molecular dynamics.

__Parameters:__


n (int) : specifies the number of steps (?) to trigger update

See also: `updateAt(...)` in Dihedrals.java

<h2 id="refine_wo_imp.refine.setForces">setForces</h2>

```python
refine.setForces(self, robson=None, repel=None, elec=None, dis=None, tors=None, dih=None, irp=None, shift=None, bondWt=None)
```
Setter method that initializes the molecular forces
specified and sets force weight for molecular dynamics.

__Parameters:__


* robson (float) : ...
* repel (float) : ...
* elec (float) : ...
* dis (float) : ...
* tors (float) : ...
* dih (float) : ...
* shift (float) : ...
* bondWt (float) : ...

See also: `setForceWeight(...)` in EnergyList.java

<h2 id="refine_wo_imp.refine.getForces">getForces</h2>

```python
refine.getForces(self)
```
Getter method to retrieve forces in a single string.

__Return:__


* output (string) : string that contains values of the calculated forces

See also: Force getter methods in ForceWeight.java

<h2 id="refine_wo_imp.refine.getAtom">getAtom</h2>

```python
refine.getAtom(self, atomTuple)
```
Getter method to retrieve atom entity object reference.

__Parameters:__


atomTuple (tuple) : contains atom entity and name of the atom

__Returns:__


atom (Atom) : atom object reference

<h2 id="refine_wo_imp.refine.printPars">printPars</h2>

```python
refine.printPars(self)
```
Utility getter methods to print out a tuple
containing values for the following parameters:

* CoarseGrain (bool)
* IncludeH (bool)
* HardSphere (double)
* DeltaStart (int)
* DeltaEnd (int)
* ShrinkValue (double)
* ShrinkH (double)
* DistanceLimit (double)

<h2 id="refine_wo_imp.refine.getEntityTreeStartAtom">getEntityTreeStartAtom</h2>

```python
refine.getEntityTreeStartAtom(self, entity)
```
Getter method to retrieve the starting atom that would be used by
AngleTreeGenerator if no atom is specified.

__Return:__

* entryAtom (Entity) : entity object reference

<h2 id="refine_wo_imp.refine.addSuiteAngles">addSuiteAngles</h2>

```python
refine.addSuiteAngles(self, fileName)
```
Utility method used to append name of a suite angle file onto an empty array assigned to
instance variable 'suiteAngleFiles'.

__Parameters:__


* fileName (string) : string that corresponds to suite angle file

<h2 id="refine_wo_imp.refine.predictShifts">predictShifts</h2>

```python
refine.predictShifts(self)
```
Predict chemical shifts using standard reference shifts specified
in a hashmap within this method. (?)

__Returns:__


shifts (list) : a list of shifts

<h2 id="refine_wo_imp.refine.setShifts">setShifts</h2>

```python
refine.setShifts(self, shiftFile)
```
Setter method that reads chemical shifts from file and returns shifts in an array.

__Parameters:__


shiftFile (string) : chemical shifts file

__Returns:__


shifts (list) : shifts retrieved from the file in the form of a list.

<h2 id="refine_wo_imp.refine.setup">setup</h2>

```python
refine.setup(self, homeDir, seed, writeTrajectory=False, usePseudo=False, useShifts=False)
```
Set up parameters and methods to run program and generate structure.

__Parameters:__


* homeDir (string) : ...
* seed (int) : ...
* writeTrajectory (bool) : ...
* usePseudo (bool) : ....
* useShifts (bool) : ....

<h2 id="refine_wo_imp.refine.addRingClosures">addRingClosures</h2>

```python
refine.addRingClosures(self)
```
Close ring structure using distance constraint on specified atoms within ring.
<h2 id="refine_wo_imp.refine.polish">polish</h2>

```python
refine.polish(self, steps, usePseudo=False, stage1={})
```
Calls the functions relevant for generation of structures...?
__Parameters:__


* steps (int) : ???
* usePseudo (bool) : ???
* stage1 (dict) : ???

<h2 id="refine_wo_imp.refine.output">output</h2>

```python
refine.output(self)
```
Prints out energy and execution time to the commandline during nmrfxstructure calculation
execution. Handles parameters for various methods if output directory has been generated.

<h2 id="refine_wo_imp.refine.dumpDis">dumpDis</h2>

```python
refine.dumpDis(self, fileName, delta=0.5, atomPat='*.H*', maxDis=4.5, prob=1.1, fixLower=0.0)
```
Writes a dump file containing distance violations based on input distance
constraints and actual distance between atoms.

__Parameters:__


* fileName (string) : name of the output dump file
* delta (float) : ...
* atomPat (string) : ...
* maxDis (float) : ...
* prob (float) : ...
* fixLower (float) : ...

<h2 id="refine_wo_imp.refine.dumpAngles">dumpAngles</h2>

```python
refine.dumpAngles(self, fileName, delta=10)
```
Writes a dump file containing dihedral violations based on input
dihedral constraints and actual dihedral measured.

__Parameters:__


* fileName (string) : name of angles file
* delta (int) : ...


<h2 id="refine_wo_imp.refine.setPeptideDihedrals">setPeptideDihedrals</h2>

```python
refine.setPeptideDihedrals(self, phi, psi)
```
Using specified phi and psi angles to calculate dihedral angle and generate coordinates.

__Parameters:__

* phi (float) : rotation angles around bonds b/t N - Calpha
* psi (float) : rotation angles around bonds b/t Calpha - C

