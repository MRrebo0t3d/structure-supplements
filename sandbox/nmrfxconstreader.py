class NMRFxReader:

    def __init__(self, fileName):
	self.fileName = fileName
	self.checker = {}
	self.constraints = []

    def distReader(self):
	with open(self.fileName, 'r') as fInput:
	    fRead = fInput.readlines()
	    for line in fRead:
		splitList = line.split("\t")
		group = splitList[1]
		atomPair = splitList[2:4]
		if group in self.checker:
		    self.constraints.append((group, tuple(atomPair)) 
		    continue
		self.checker[group] = list(map(float, splitList[-2:]))
		self.constraints.append((group, tuple(atomPair), self.checker[group]))
	return self.constraints

