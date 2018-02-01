import csv
import os
from  lib.restobyIPfunctions import restobyIP_OutputFile
from lib.createTsvReadingFile import createTsvReadingFile
from lib.defineFoldersandFiles import foldersFilesNames

print('\n\n Routine in progress. Please Wait \n\n')
####################### Folder & Files Definitions #############################
inputFolder = foldersFilesNames("inputFolder")
outputFolder = foldersFilesNames("outputFolder")
filenameLog = foldersFilesNames("filenameLog")
tsvFolder = foldersFilesNames("tsvFolder")
filenameOutput = foldersFilesNames("filenameOutputResto")
filenameIP = foldersFilesNames("filenameBadIP")
cwd = os.getcwd()

######################Create .tsv file with configuration#######################
createTsvReadingFile(filenameLog)

#########################Vreate .txt Output File###############################
with open(os.path.join(cwd, tsvFolder, filenameLog) + ".tsv") as tsvfile:
    # IP Address under which all items are being restored
    with open(os.path.join(cwd, inputFolder, filenameIP) + ".input") as IPfile:
        for ip in IPfile:
            if ip.find('##') == -1: #if it is not a comment line
                restobyIP_OutputFile(csv.DictReader(tsvfile, dialect="excel-tab"),
                 os.path.join(cwd, inputFolder, filenameOutput) + ".input",
                  ip)
###############################################################################
print("File " + filenameOutput + ".input" " created Successfully")
