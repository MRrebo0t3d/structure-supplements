import sys, csv
from refine import *
from org.nmrfx.structure.chemistry import MolFilter
from org.nmrfx.structure.chemistry import Molecule

"""This program is used to filter ambiguous constraints by determining which atom pairs contain the smallest distance"""

pdb = sys.argv[1]
AConstraintFile = sys.argv[2]
refiner = refine()
mol = refiner.readPDBFile(pdb)

def findLowestConst(dictOfResConst):
	try:
		distances = dictOfResConst["distPerConst"]
	except KeyError:
		return -1
	distances = dictOfResConst["distPerConst"]
	keyOfSmallestDis=distances.index(min(distances))
	
	#returns a tuple with the contraint out of the pair with the smallest distance b/t atoms and the distance.
	return (dictOfResConst[keyOfSmallestDis],keyOfSmallestDis)

	#smallestDis = sortedDistances[0]
	#for i,val in enumerate(distances):
	#	if val == smallestDis:
			#print dictOfResConst[i]
	#		print (dictOfResConst[i],i,smallestDis)
	#		return (dictOfResConst[i],i,smallestDis)
			

def calcDistPerConstraintLine(dictOfResConst):
	"""This function calculates distances for each pair of contraints passed after converting them using convertResAtom()."""
	distances = []
	for key in dictOfResConst:
		l = dictOfResConst[key]
		string1 = '.'.join(l[:2])
		string2 = '.'.join(l[2:-1])
		#print (string1, string2)
		mf1 = MolFilter(string1)
		mf2 = MolFilter(string2)
		dis = Molecule.calcDistance(mf1, mf2)
		distances.append(dis)
	dictOfResConst["distPerConst"] = distances

	#after calculating distances between atom for each pair, it develops a list of distances, index of distance value corresponds to key of constraint.
	#retuns a dictionary with a new key, 'distPerConst', which contains list of distances.
	#ex: {0: ['28', 'HB*', '17', 'HB*', '4.83'], 1: ['1', 'HE*', '17', 'HB*', '4.83'], 'distPerConst': [11.04948701172241, 5.033537446192507]}
	return dictOfResConst

def convertResAtom(dictOfResInfo):
	"""This function will convert the Q's in residue atoms into H's and will return a string to pass into MolFilter()."""
	for key in dictOfResInfo:
		for ind,string in enumerate(dictOfResInfo[key]):
			if 'QQ' in string:
				string = string.replace('QQ','H')
				string += '*'
				dictOfResInfo[key][ind] = string
				continue
			if 'Q' in string:
				string = string.replace('Q','H')
				string += '*'
				dictOfResInfo[key][ind] = string
			elif 'H' in string:
				if '1' in string or '2' in string or '3' in string:
					string += '*'
					dictOfResInfo[key][ind] = string
				elif 'B' in string:
                                        string += '*'
                                        dictOfResInfo[key][ind] = string
	#returns a dictionary pretty much like the one returned by getResInfo(). However, the atoms are converted into a form that MolFilter() can use.
	#ex: {0: ['1', 'HB*', '2', 'H', '3.79'], 1: ['63', 'HB2*', '2', 'H', '3.79']}
	return dictOfResInfo

def getResInfo(contraintList):
	"""This function will take as input a pair from list of pairs and grab residue info relevant. The zero values of all alternative distance constraints is changed to the
	corresponding nonzero value. That is, if the pair contains an alternative distance contraint with a value of zero and there is a nonzero value for an alternative contraint,
	the nonzero value replace the zero value.
	"""
	resInfoDictionary = {}
	savingNonZ=''
	for i,string in enumerate(contraintList):
		listOfConstInfo = []
		splitString = string.split()

		if splitString[-1] != '0.00':
			savingNonZ = splitString[-1]
		elif splitString[-1] == '0.00' and savingNonZ != '':
			splitString[-1] = savingNonZ

		listOfConstInfo.extend([splitString[0],splitString[2],splitString[3],splitString[5],splitString[6]])
		resInfoDictionary[i] = listOfConstInfo	

	#returns a dictionary for each pair in list of pairs
	#ex: {0: ['1', 'QB', '2', 'H', '3.79'], 1: ['63', 'HB2', '2', 'H', '3.79']}
	return resInfoDictionary

def removeDuplicateLines(fileName):
	"""This function takes in a file and creates a new file that contains a single occurence of the each line, removing all duplicates"""
	exten = fileName.split(".")[-1]
	outputFile="AmbiConstWODup."+exten
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

	#returns a list of lists of strings.
	# ex: [['  1 MET  QB      2 GLN  H       3.79', ' 63 LYS  HB2     2 GLN  H       0.00'], ['  1 MET  HB2     3 ILE  QG2     5.79', ' 29 LYS  HB2     3 ILE  QG2     0.00'], ...]
	return listOfPairs

def runTest(ambiConstFileName):
	"""This function will call all of the functions created in this script upon completion"""
	try:
		#newFileWODup = removeDuplicateLines(ambiConstFileName)
		#print newFileWODup
		lstOfPairs = pairAmbiConst(ambiConstFileName)
	except:
		return -200
	ext=ambiConstFileName.split('.')[-1]
	finalFileName="testDisOutput."+ext
	with open(finalFileName,"wb") as finalFile:
	#going through each pair in list of pairs returned
		for index,pair in enumerate(lstOfPairs):
			#finalInfo = {}
			resInfoDict = getResInfo(pair)
			convertedResInfoDict = convertResAtom(resInfoDict)
			dictOfResConst = calcDistPerConstraintLine(convertedResInfoDict)
#		if dictOfResInfo != -1:
			lowestConstOfPair,indForSmallDis = findLowestConst(dictOfResConst)
#		else: return -100
#		indForLower = findLowestConst(dictOfResConst)[1]
			constWSmallestDis = pair[indForSmallDis]
			tempStr = constWSmallestDis.split(" ")
			if float(tempStr[-1]) != float(lowestConstOfPair[-1]):
				tempStr[-1] = lowestConstOfPair[-1]
			resStr = " ".join(tempStr)
			finalFile.write(resStr+"\n")

#		finalInfo[""] = lowestConstOfPair
#		finalInfo["constWSmallestDis"] = constWSmallestDis
#		finalInfo["SmallestDis"] = findLowestConst(dictOfResConst)[2]
#		finalList.append(finalInfo)
#

	return finalFileName


print runTest(AConstraintFile)

#commented code blocks
"""		firstAtom = resRaw[1]
		secAtom = resRaw[-2]
		mid = len(tempStr)/2
if "Q" in val:
	if j <= mid:
		tempStr[j] = firstAtom
	else:
		tempStr[j] = secAtom
		tempStr[-1] = resRaw[-1]
		resStr = " ".join(tempStr)
		continue
	elif "H" in val:
        	if '1' in val or '2' in val or '3' in val:
        		if j <= mid:
        		tempStr[j] = firstAtom
        	else:
       			tempStr[j] = secAtom
        		tempStr[-1] = resRaw[-1]
        		resStr = " ".join(tempStr)
        		continue"""
