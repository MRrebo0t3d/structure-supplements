import sys,csv

f = sys.argv[1]

def removeDuplicateLines(fileName):
        """This function takes in a file and creates a new file that contains a single occurence of the each line, removing all duplicates"""
        exten = fileName.split(".")[-1]
        outputFile="ambi_const_file_without_dup."+exten
        linesSeen = set()
        with open(outputFile,"wb") as outFile:
                for line in open(fileName,"rb"):
                        if line not in linesSeen:
                                outFile.write(line)
                                linesSeen.add(line)
        return outputFile

def pairAmbiConst(fileName):
        """This function takes in a file with ambiguous contraints and pairs the alternative possibilities for each ambiguous contraint. It returns a list of lists
        of paired ambiguous contraints."""
        listOfPairs = []
        with open(fileName,"rb") as inFile:
                reader = csv.reader(inFile,delimiter="\n")
                readerList = list(reader)
                fileAsList = [row[0].split() for row in readerList]
                for i,_ in enumerate(fileAsList):
                        if fileAsList[i][-1] != "0.00":
                                pair = []
                                pair.append(readerList[i][0])
                                k=1
                                if fileAsList[i+k][-1] == "0.00":
                                        while fileAsList[i+k][-1] == "0.00":
                                                pair.append(readerList[i+k][0])
                                                k+=1
                                                if (i+k) >= len(fileAsList):
                                                        break
                                listOfPairs.append(pair)
        for elem in listOfPairs:
               print elem
        #print "-------------------------"

        #return listOfPairs




print pairAmbiConst(f)

#removeDuplicateLines(f)
