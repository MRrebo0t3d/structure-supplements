
import csv,sys

fullFile = sys.argv[1]


def extractor(fileName):
    """ This function takes a regular distance constraint file
    generates an ambiguous constraint file, with only ambiguous constraints, and
    a test distance constraint file to use when ambiguous constraint file has been filtered.
    The filtered ambiguous constraints will be appended to the test distance constraint file created
    in this function."""

    ext = fileName.split(".")[-1]
    outputFileName1 = "ambi_const_file."+ext
    outputFileName2 = "test_distances."+ext
    with open(fileName,"rb") as inFile:
        with open(outputFileName1,"wb") as outFile1:
            with open(outputFileName2,"wb") as outFile2:
                reader = csv.reader(inFile,delimiter="\n")
                readerList = list(reader)
                fileAsList = [row[0].split() for row in readerList]
                for i,_ in enumerate(fileAsList):
                    k = 1
                    if (i+k) < len(fileAsList):
                        if fileAsList[i][-1] != "0.00" and fileAsList[i+k][-1] =="0.00":
                            outFile1.write(readerList[i][0]+"\n")
                            while fileAsList[i+k][-1] == "0.00":
                                outFile1.write(readerList[i+k][0]+"\n")
                                k+=1
                                if (i+k) >= len(fileAsList):
                                    break
                        elif fileAsList[i][-1] != "0.00" and fileAsList[i+k][-1] != "0.00":
                            outFile2.write(readerList[i][0]+"\n")
                    if i == (len(fileAsList)-1) and fileAsList[i][-1] != "0.00":
                        outFile2.write(readerList[i][0]+"\n")

    return (outputFileName1,outputFileName2)

print extractor(fullFile)

