import csv,sys

fullFile = sys.argv[1]


def extractor(fileName):
    ext = fileName.split(".")[-1]
    outputFileName = "DIST."+ext
    with open(fileName,"rb") as inFile:
        with open(outputFileName,"wb") as outFile:
            reader = csv.reader(inFile,delimiter="\n")
            readerList = list(reader)
            fileAsList = [row[0].split(" ") for row in readerList]
            for i,_ in enumerate(fileAsList):
                if "H21" in fileAsList[i] and "H22" in fileAsList[i]:
                    indexFortyOne = fileAsList[i].index("H21")
                    indexFortyTwo = fileAsList[i].index("H22")
                    fileAsList[i][indexFortyOne] = "H22"
                    fileAsList[i][indexFortyTwo] = "H21"
                else:
		    if "H21" in fileAsList[i]:
                        indexOfVal = fileAsList[i].index("H21")
                        fileAsList[i][indexOfVal] = "H22"
		    elif "H22" in fileAsList[i]:
                        indexOfVal = fileAsList[i].index("H22")
                        fileAsList[i][indexOfVal] = "H21"

                outFile.write(" ".join(fileAsList[i])+"\n")

	return outputFileName

print extractor(fullFile)
