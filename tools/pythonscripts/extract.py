import sys

fileName = sys.argv[1]

def getModelFromPDB(file):
	file = str(file)
	exten = file.split(".")[-1]
	import csv
	with open(file,"rb") as inFile:
		with open("pdbModel1."+exten,"wb") as outFile:
			reader = csv.reader(inFile,delimiter="\n")
			writeFile = csv.writer(outFile)
			for line in reader:
				if "MODEL        1" in line[0]:
					for line in reader:
						if "ENDMDL" not in line[0]:
							print line[0]
						else:
							break
					break
	return ""
print getModelFromPDB(fileName)
