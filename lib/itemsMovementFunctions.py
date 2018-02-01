import csv
from lib.defineEntries import defineEntries


##########################Defines Config for TSV file###########################
def getMvmntEntries(row):
    entries = defineEntries(row, 'itemMvmnt')
    event  = entries['event']
    date = entries['date']
    timeStamp =  entries['time']

    try:
        itemName = entries['itemName'].split('[')[2].split(']')[0];
    except:
        itemName  = entries['itemName'].split('[')[1].split(']')[0]

    if (len(entries['itemName'].split('['))) == 4: #In case there is a Fantasy/Costume Item Name
        itemName  = entries['itemName'].split('[')[3].split(']')[0] + entries['itemName'].split('[')[3].split(']')[1]


    char = entries['tradeAlz'].split('[')[1].split(']')[0]

    if (entries['event'].find('AlzTransfreByTrade(Take)') != -1):
        itemName  = entries['itemName'].split('[')[1].split(']')[0]
        string = [date, timeStamp, 'Trade', 'Receive' , itemName, 'From Char:',char]

    elif (entries['event'].find('AlzTransferByTrade(Give)') != -1):
        itemName  = entries['itemName'].split('[')[1].split(']')[0]
        string = [date, timeStamp, 'Trade', 'Send' , itemName, 'To Char:',char]

    elif (entries['event'].find('Mail-AlzReceive') != -1):
        itemName  = entries['itemName'].split('[')[1].split(']')[0]
        string = [date, timeStamp, 'Mail', 'Receive' , itemName, 'From Char:',char]

    elif (entries['event'].find('Mail-AlzAttached') != -1):
        itemName  = entries['itemName'].split('[')[1].split(']')[0]
        string = [date, timeStamp, 'Mail', 'Send' , itemName, 'To Char:',char]

    elif (entries['event'].find('WarehouseAlzDepositWithdraw(+/-)') != -1):
        itemName  = entries['itemName'].split('[')[1].split(']')[0]
        string = [date, timeStamp, 'Warehouse', '+/-' , itemName]

    elif (entries['event'].find('ItemTransferByTrade(Give)') != -1):
         # itemName = entries['itemName'].split('[')[2].split(']')[0];
         char = entries['tradeItem'].split('[')[1].split(']')[0]
         string = [date, timeStamp, 'Trade', 'Send' , itemName, 'To Char:',char]

    elif (entries['event'].find('ItemTransferByTrade(Take)') != -1):
         # itemName = entries['itemName'].split('[')[2].split(']')[0];
         char = entries['tradeItem'].split('[')[1].split(']')[0]
         string = [date, timeStamp, 'Trade', 'Receive' , itemName, 'From Char:',char]

    elif (entries['event'].find('SendItembyMail') != -1):
         #itemName = entries['itemName'].split('[')[2].split(']')[0];
         char = entries['mailItem'].split('[')[1].split(']')[0]
         string = [date, timeStamp, 'Mail', 'Send' , itemName, 'To Char:',char]

    elif (entries['event'].find('ReceiveItembyMail') != -1):
         # itemName = entries['itemName'].split('[')[2].split(']')[0];
         char = entries['mailItem'].split('[')[1].split(']')[0]
         string = [date, timeStamp, 'Mail', 'Receive' , itemName, 'From Char:',char]

    elif (entries['event'].find('ItemLoot') != -1 and entries['event'].find('PartyQuestItemLooting') == -1):
         # itemName = entries['itemName'].split('[')[2].split(']')[0];
         world = entries['world'].split('[')[2].split(']')[0];
         string = [date, timeStamp, 'Loot', 'Picked' , itemName, 'Map:', world]

    elif (entries['event'].find('ItemDrop') != -1):
         # itemName = entries['itemName'].split('[')[2].split(']')[0];
         world = entries['world'].split('[')[2].split(']')[0];
         string = [date, timeStamp, 'Drop', 'Dropped' , itemName, 'Map:', world]

    elif (entries['event'].find('ItemSell') != -1):
         # itemName = entries['itemName'].split('[')[2].split(']')[0];
         value = entries['npcSell'].split('[')[1].split(']')[0]
         string = [date, timeStamp, 'NPC Sell', 'Sell' , itemName, '','','Price:',value]

    elif (entries['event'].find('ItemDestroy(Original)') != -1):
         # itemName = entries['itemName'].split('[')[2].split(']')[0];
         value = entries['npcSell'].split('[')[1].split(']')[0]
         string = [date, timeStamp, 'Item Destroyed', 'Destroy' , itemName]

    elif (entries['event'].find('ChaosUpgradeResult(Destroyed)') != -1):
         # itemName = entries['itemName'].split('[')[2].split(']')[0];
         value = entries['npcSell'].split('[')[1].split(']')[0]
         string = [date, timeStamp, 'Chaos Upgrade Destroyed', 'Destroy' , itemName]

    elif (entries['event'].find('PersonalShopSell') != -1):
         # itemName = entries['itemName'].split('[')[2].split(']')[0];
         value = entries['PersonalShop'][1].split('[')[1].split(']')[0]
         char = entries['PersonalShop'][2].split('[')[1].split(']')[0]
         string = [date, timeStamp, 'Personal Shop', 'Sell' , itemName,'To Char:',char, 'Price:',value]

    elif (entries['event'].find('PersonalShopBuy') != -1):
         #itemName = entries['itemName'].split('[')[2].split(']')[0];
         value = entries['PersonalShop'][1].split('[')[1].split(']')[0]
         char = entries['PersonalShop'][2].split('[')[1].split(']')[0]
         string = [date, timeStamp, 'Personal Shop', 'Buy' , itemName,'From Char:',char, 'Price:',value]

    elif (entries['event'].find('AgentShopBuyRequest') != -1):
         # itemName = entries['itemName'].split('[')[2].split(']')[0];
         value = entries['AgentShop'][1].split('[')[1].split(']')[0]
         char = entries['AgentShop'][0].split('[')[1].split(']')[0]
         count = entries['AgentShop'][2].split('[')[1].split(']')[0]
         string = [date, timeStamp, 'Agent Shop', 'Buy' , itemName,'From Char:',char, 'Price:',value, 'Count:', count]

    elif (entries['event'].find('AgentShopSellRequest') != -1):
         # itemName = entries['itemName'].split('[')[2].split(']')[0];
         value = entries['AgentShop'][1].split('[')[1].split(']')[0]
         char = entries['AgentShop'][0].split('[')[1].split(']')[0]
         count = entries['AgentShop'][2].split('[')[1].split(']')[0]
         string = [date, timeStamp, 'Agent Shop', 'Sell' , itemName,'To Char:',char, 'Price:',value, 'Count:', count]


    else:
        string = []

    return string

################### Write .tsv file, ordered by data and time##################
def writeTsvFile(filename, readerEntry):
    with open(filename + ".tsv", "w+") as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
        writer.writerow(['Date', 'Time', 'Type', 'Action', 'Item', 'Type2', 'Type3', 'Type4', 'Price', 'Type5', 'Count'])
        for row in readerEntry:
            string = getMvmntEntries(row);
            if len(string) != 0 :
                writer.writerow(string)
###############Create file with item movement grouped by type###################
def createDictGroupedbyType(filename):
    with open(filename + ".tsv") as tsvfile:
        readerNew = csv.DictReader(tsvfile, dialect="excel-tab")
        string = '';
        itemStringData = {};

        for line in readerNew:
            if line['Type'] in itemStringData: #if data entry already exists, just appends the new entry
                for key, value in line.items():
                    if type(value) == str:
                        string += value + '\t' ;
                itemStringData[line['Type']].append(string);
            else:
                itemStringData[line['Type']]=[]; #if the dict  does not have that event type, create and then append
                for key, value in line.items():
                    if type(value) == str:
                        string += value + '\t' ;
                itemStringData[line['Type']].append(string);
            string = '';
        return itemStringData

###############Create file with item movement grouped by type###################
def writeTxtFile(filename, filenameTsv):
    with open(filename + ".output", "w+") as txtfile:
        itemStringData = createDictGroupedbyType(filenameTsv)
        for key, value in itemStringData.items():
            txtfile.write(key + '\n')
            for i in range(0, len(value)):
                txtfile.write(value[i] + '\n')
            txtfile.write('\n')

################################################################################
def writeOutputMVMTFile(readerEntry, filenameTxt, filenameTsv):

    writeTsvFile(filenameTsv, readerEntry)
    writeTxtFile(filenameTxt, filenameTsv)
