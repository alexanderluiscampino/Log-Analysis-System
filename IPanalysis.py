import csv
import os
from lib.IPanalysisFunctions import writeOutputIPanalysis
from lib.createTsvReadingFile import createTsvReadingFile
from lib.defineFoldersandFiles import foldersFilesNames

print('\n\n Routine in progress. Please Wait \n\n')

####################### Folder & Files Definitions #############################
inputFolder = foldersFilesNames("inputFolder")
outputFolder = foldersFilesNames("outputFolder")
filenameLog = foldersFilesNames("filenameLog")
tsvFolder = foldersFilesNames("tsvFolder")
filenameOutput = foldersFilesNames("filenameOutputIP")
filenameIP = foldersFilesNames("filenameBadIP")
cwd = os.getcwd()

######################Create .tsv file with configuration#######################
createTsvReadingFile(filenameLog)

#########################Read file and retrieve line values#####################
#Initiate Variables
entriesLookFor = ['CharListRequest','CharINITfromClientResult'] #In case of different logs
exit = 0;
i = 0;

while exit == 0:
    with open(os.path.join(cwd, tsvFolder, filenameLog) + ".tsv") as tsvfile:
        exit = writeOutputIPanalysis(csv.DictReader(tsvfile, dialect="excel-tab"),
            os.path.join(cwd, outputFolder, filenameOutput) + ".output",
            entriesLookFor[i])
    i += 1;

print("File " + filenameOutput + ".output" " created Successfully")
