import csv
import os
import csv, sys, operator
from  lib.itemsMovementFunctions import writeOutputMVMTFile
from lib.createTsvReadingFile import createTsvReadingFile
from lib.defineFoldersandFiles import foldersFilesNames

print('\n\n Routine in progress. Please Wait \n\n')
####################### Folder & Files Definitions #############################
inputFolder = foldersFilesNames("inputFolder")
outputFolder = foldersFilesNames("outputFolder")
filenameLog = foldersFilesNames("filenameLog")
filenameOutput = foldersFilesNames("filenameOutputMVMT")
tsvFolder = foldersFilesNames("tsvFolder")
cwd = os.getcwd()

############################ Create .tsv log file ##############################
createTsvReadingFile(filenameLog)

#########################Vreate .txt Output File###############################
with open(os.path.join(cwd, tsvFolder, filenameLog) + ".tsv") as tsvfile:
     writeOutputMVMTFile(csv.DictReader(tsvfile, dialect="excel-tab")
     , os.path.join(cwd, outputFolder, filenameOutput),
      os.path.join(cwd, tsvFolder, filenameOutput))


print("File " + filenameOutput + ".output" " created Successfully")
print("File " + filenameOutput + ".tsv" " created Successfully")
