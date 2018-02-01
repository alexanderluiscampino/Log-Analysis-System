import csv
import os
from lib.defineFoldersandFiles import foldersFilesNames

################################################################################
inputFolder = foldersFilesNames("inputFolder")
tsvFolder = foldersFilesNames("tsvFolder") #to store .tsv file created with the log
cwd = os.getcwd() # current working directory

########################## Create .tsv log file ################################
def createTsvReadingFile(filename):
    with open(os.path.join(cwd, inputFolder, filename) + ".input") as inputFile:
        with open(os.path.join(cwd, tsvFolder, filename) + ".tsv", "w+") as tsvFile:
            logHeaders='';
            for i in range(1,20):
                logHeaders += "column" + str(i) + '\t'
            tsvFile.write(logHeaders + "\n")
            for line in inputFile:
                tsvFile.write(line)
