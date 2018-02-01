import csv
import os

def createTsvReadingFile(filename):
    with open(filename + ".input") as inputFile:
        with open(filename + ".tsv", "w+") as tsvFile:
            logHeaders='';
            for i in range(1,20):
                logHeaders += "column" + str(i) + '\t'
            tsvFile.write(logHeaders + "\n")
            for line in inputFile:
                tsvFile.write(line)
