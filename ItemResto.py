import csv
import os
from  lib.itemRestoFunctions import WritePBitemFile
from lib.createTsvReadingFile import createTsvReadingFile
from lib.defineFoldersandFiles import foldersFilesNames

print('\n\n Routine in progress. Please Wait \n\n')

####################### Folder & Files Definitions #############################
inputFolder = foldersFilesNames("inputFolder")
outputFolder = foldersFilesNames("outputFolder")
filenameLog = foldersFilesNames("filenameLog")
filenameOutput = foldersFilesNames("filenameOutputResto")
tsvFolder = foldersFilesNames("tsvFolder")
cwd = os.getcwd()

createTsvReadingFile(filenameOutput)
#########################Read file and retrieve line values#####################
with open(os.path.join(cwd, tsvFolder, filenameOutput) + ".tsv") as tsvfile:
     # Write output file
     WritePBitemFile(csv.DictReader(tsvfile, dialect="excel-tab"),
      os.path.join(cwd, outputFolder, filenameOutput))


print("File " + filenameOutput + ".item" " created Successfully")
print("File " + filenameOutput + ".tsv" " created Successfully")
print("File " + filenameOutput + ".output" " created Successfully")
