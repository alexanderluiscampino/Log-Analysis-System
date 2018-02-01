import csv
import os
from  lib.DungeonAnalysisFunctions import writeOutputDungeonAnalysis
from lib.createTsvReadingFile import createTsvReadingFile
from lib.defineFoldersandFiles import foldersFilesNames

print('\n\n Routine in progress. Please Wait \n\n')
####################### Folder & Files Definitions #############################
inputFolder = foldersFilesNames("inputFolder")
outputFolder = foldersFilesNames("outputFolder")
filenameLog = foldersFilesNames("filenameLog")
filenameOutput = foldersFilesNames("filenameOutputDG")
tsvFolder = foldersFilesNames("tsvFolder")
cwd = os.getcwd()

############################ Create .tsv log file ##############################
createTsvReadingFile(filenameLog)

############################ Creates Output file ###############################
with open(os.path.join(cwd, tsvFolder, filenameLog) + ".tsv") as tsvfile:
     writeOutputDungeonAnalysis(csv.DictReader(tsvfile, dialect="excel-tab")
     ,os.path.join(cwd, outputFolder, filenameOutput))

print("File " + filenameOutput + ".output" " created Successfully")
