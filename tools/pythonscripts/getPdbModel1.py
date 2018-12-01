import sys,csv

pdbFile = sys.argv[1]

def getModel1FromPDB(fileName):
    ext = fileName.split(".")[-1]
    outputFileName = "pdbModel1."+ext
    with open(fileName,"rb") as inFile:
        with open(outputFileName,"wb") as outFile:
            reader = list(csv.reader(inFile,delimiter="\n"))
            copiedModel1 = False
	    k = 1
	    for index,line in enumerate(reader):
		if "MODEL" in line[0].split() and "1" in line[0].split():
		    while "ENDMDL" not in reader[index+k][0].split():
			outFile.write(reader[index+k][0] + "\n")
			k+=1
			if "ENDMDL" in reader[index+k][0]:
			    copiedModel1 = True
		if copiedModel1 ==True:
		    break
    return outputFileName

print getModel1FromPDB(pdbFile)
