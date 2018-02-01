from lib.defineEntries import defineEntries
import csv
################ Define Variables to use in Functions ##########################
# Define event entries of interest
resto_entries = ['ItemTransferByTrade(Give)',
                'SendItembyMail',
                'AlzTransferByTrade(Give)',
                'Mail-AlzAttached',
                'SendItembyMail',
                'ItemDrop',
                'ItemDestroy(Original)',
                'ChaosUpgradeResult(Destroyed)',
                'ItemSell']

# Fieldnames to save on itemList.tsv as headers
fieldnames = []
for i in range(1,20):
   fieldnames.append("column" + str(i))
fieldnames.append('')

############### Define which entries to write to file ##########################
def restobyIP_OutputFile(reader, filename, badIPaddress):

    resto = 0;
    with open(filename, 'w+') as csvfile:
        for row in reader:
             entries = defineEntries(row, 'IP')

             if entries['event'] == 'CharListRequest' or entries['event'] == 'CharINITfromClientResult':
                 if entries['IPAddress'].find(badIPaddress) > 0:
                     resto = 1;
                 else:
                     resto = 0;

             if resto == 1 and entries['event'] in resto_entries:
                 writeItemListFile(row,csvfile)

######################### Write entry on file #################################
def writeItemListFile(row, csvfile):
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect = 'excel-tab')
    writer.writerow(row)
