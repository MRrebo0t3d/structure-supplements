# Project Files

*Sample directory structure:*

    project.yaml      # Configuration file
    input/            # Directory with all of the constraints and molecular structure information
         pdbID.seq    # Sequence file (i.e. 2koc.seq)
         dihedrals.*  # Dihedral constraints (XPLOR, CYANA, or STAR)
         distances.*  # Distance constraints (XPLOR, CYANA, or STAR)
         ...

The sample directory structure shown above illustrates an example of how files can be organized. The input directory contains information about the constraints relevant to calculate a structure. The molecular structure, constraints, and annealing parameters are defined in a project file.  This file uses the YAML (Yaml Ain't Markup Language) format.  YAML is a human readable data format that has a defined structure.  Unlike many markup or data languages, it is free from a lot of actual markup fluff which makes it easy to read (and write).  Despite the apparent simplicity, remember that there is a defined formalism that must be followed.  For NMRFx Structure, you don't need to know much about YAML files, you can simply work from existing examples.

The project file is best understood by reference to an example:

    # Note the "key : value" syntax and evenly indented sections.

    molecule :                            # supported section (list of supported sections below)
        sequence : GGCUCUGGUGAGAGCCAGAGCC  
        residues : '1:2 125:135 217:225'
        ptype : RNA                       

    distances:
        -                                 # hyphen character indicates elements below it are in list
          file : constraints1
          type : cyana
        -                                 # This is a separate list for different file of constraints
          file : constraints2
          type : cyana

    angles:
        -
          file : constraints.aco
          type : cyana

    rna:
        ribose : Constrain

    anneal:
        steps : 15000
        highTemp : 5000.0

As used in NMRFx, the ".yaml" file adopts two primary uses of the YAML syntax.  Elements are syntaxed in a "_key : value_" pair relationship used to set values of parameters (keys).  So, *sequence : GGUCU...*, indicates that the RNA (in this case) sequence is to be set to the value *GGCU...*.  The value for a key can itself contain multiple key/value pairs.  For example, the molecule section has multiple parameters (sequence, residues etc.).  The hyphen (**-**) characters precede elements of a list.  This example, has two distance constraint sections. 

It's important to note that YAML files use indentation to define the structure and that indenting should be done with multiple space characters, rather than tabs. The specific number of spaces does not matter, but elements nested at the same level should have a consistent number of spaces.

**The currently supported sections are listed below :**

1. **molecule**
:   This section specifies the molecular toplogy.  The polymer sequence can be specified directly in the ".yaml" file as shown here, or in an nvj style sequence file (using a file parameter).

        sequence : *sequence*
          """The sequence in single letter code form."""

        file : *fileName*
          """The path to a text file containing the sequence."""

        ptype : *RNA* or *protein*
          """The type of polymer sequence."""

        type : *nv* or *fasta*
          """The format of the file.  Either **nv**, in which it is the NMRViewJ format 
             (similar to CYANA) with a single residue on each line, and an optional residue 
             number, or fasta, in which case its the FASTA format."""

        residues : *residueList*
          """By default, residues are numbered starting at 1.  
             This parameter can be used to specify some other numbering scheme. 
             Examples:

             '5'  : Start numbering at 5.
             1:2 125-130 200:207 : First two residues are numbered 1 and 2, 
             The next six residues are numbered from 125 through 130 (inclusive), 
             the remaining 8 residues are numbered from 200 through 207 (inclusive)."""
         

        link : *linkSpecifier*
          """Structure calculations require that the molecular topology be one connected tree.  
             If there are multiple chains that are represented by one sequence item you can 
             insert a break in the sequence with the link parameter.  The linkSpecifier is of 
             the form **start:nLinks**, where **start** is the residue at which to insert a break, 
             and **nLinks** is the number of linkers to use to allow flexibility between the chains."""

2. **distances**
: This section specifies distance constraints to be used.  More than one distance constraint set can be used so this section is a YAML list, with one or more elements.

        file : *fileName*
          """The path to the file containing the constraints."""

        type : *nv* or *cyana* or *xplor*
          """The format of the file.  
             The following formats are supported:
             *nv* => NMRViewJ format (similar to CYANA), 
             *cyana* => CYANA/DYANA format,
             *xplor* => XPLOR format 
             """

        range : *rangeSpecifier*
          """It can be convenient to have a file containing constraints appropriate to a 
             super set of the sequence being used.  For example, you might have distance 
             constraints for a large RNA, and want to analyze or generate structures that 
             are a fragment of the whole molecule.  The *rangeSpecifier* is used to indicate 
             that only constraints for residues within a certain range are to be used."""

3. **angles**
: This section specifies angle constraints to be used.  More than one angle constraint set can be used so this section is a YAML list, with one or more elements.

        file : *fileName*
          """ The path to the file containing the constraints. """

        type : *nv* or *cyana* or *xplor*
          """The format of the file.  
             The following formats are supported:
             *nv* => NMRViewJ format (similar to CYANA), 
             *cyana* => CYANA/DYANA format,
             *xplor* => XPLOR format 
             """

4. **rna**
: This section specifies parameters to be used when running the program using RNA structures. 

        ribose : *Constrain*
          """ If set to *Constrain*, automatically add distance constraints to maintain 
              the ribose ring in a closed state. """

        vienna : *DotBracketSequence*
          """ Specify the secondary structure using a dot-bracket (Vienna) string.  
              When performing a structure calculation this will automatically add 
              distance constraints and dihedral angle constraints to maintain helices.  
              Dihedral angle constraints will also be added for GNRA tetraloops."""

        suite : *fileName*
          """ The path to the file containing with a list of rotamer suites to be used 
              to set angle constraints. """


5. **shifts**
: This section specifies parameters to be read to calculation structure using chemical shift information.

         file : *fileName*

         type : *nv*

         range : *rangeSpecifier*

         weight : ...




6. **anneal**
: This section specifies parameters to be used when running an annealing protocol using torsion angle molecular dynamics.
        
        # Molecular dynamics parameters
        steps : *nSteps*
          """ The total number of torsion angle molecular dynamcs steps to execute. """

        highTemp : *highTemperature*
          """ The temperature to be used at the beginning of the annealing protocol. """

        irpWeight : **
          """ Pending description ... """

        # Minimization algorithm parameters
         swap : *nSteps to invoke swap of protons*
          """ Pending description ... """

