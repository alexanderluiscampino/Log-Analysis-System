import math
from lib.defineEntries import defineEntries
#########################Get Item Period#######################################
def getItemPeriod(entries):
    periodEntry = getEntryPeriod(entries);
    if periodEntry == 3:
        itemPeriod = 0; #assumes item is not periodic
    else:
        itemPeriod = entries['itemPeriod'][periodEntry].split('[')[1].split(':')
        try:
            itemPeriod = int(itemPeriod[1])
        except:
            try:
                itemPeriod = int(itemPeriod[0].split(']')[0])
            except:
                itemPeriod = 0

    return itemPeriod;
#########################Get Item Period#######################################
def getEntryPeriod(entries): #depending on the type of event, period will be on different collumn
    if (entries['event'].find('ItemDrop(User)') != -1) or (entries['event'].find('SendItembyMail') != -1):
        periodEntry = 1;
    elif (entries['event'].find('ItemTransferByTrade(Give)') != -1):
        periodEntry = 0;
    elif (entries['event'].find('ItemSell') != -1) or (entries['event'].find('ItemDestroy(Original)') != -1):
        periodEntry = 2;
    else:
        periodEntry = 3;

    return periodEntry;
#########################Get Item Kind#########################################
def getItemKind(entries):
    alzCheck = checkEventType(entries); # if the type of event is related to alz, gives potion of luck
    if alzCheck:
        itemKind = 2842;
    else:
        itemKind = getItemKindItem(entries);

    return itemKind;
#########################Define Item Kind for Items#############################
def getItemKindItem(entries):
    itemKind = int(entries['itemName'].split('[')[1].split(']')[0].split('(')[0])
    if itemKind >= 2147483647: #In case PB cant take the large number, reset to +15

        try:

            keyValues = checkKeyWords(entries);


            itemKind= int(entries['itemIndex']) + sum(keyValues)

        except:
            itemKind = 0; # if anythign goes wrong, item 0, always check output

    return itemKind

#########################Check for Event Type###################################
def checkEventType(entries): # if the event is related to sending alz
    if (entries['event'].find('Alz') == -1):
        alzCheck = 0;
    else:
        alzCheck = 1;

    return alzCheck;
#########################Find Words on Name#####################################
def checkKeyWords(entries): # this modifies the item index according to words found on item name
    keyWords = ["Accounts Belonging","Character Attribution","Equipped","Broken", "Sealed"]
    itemLevel = int(entries['itemName'].split('+')[1].split(',')[0].split('(')[0]) #+level of item

    keyValues =[itemLevel*8192, 4096, 524288, 1048576, 134217728, 268435456]# hardcoded itemKind numbers, retrieved from PB
    i=1
    for word in keyWords:
        if (entries['itemName'].find(word) == -1):
            keyValues[i] = keyValues[i] *0
            #keyBools.append(0)
        else:
            keyValues[i]  = keyValues[i] *1
            #keyBools.append(1)
        i+=1


    return keyValues;
#########################Define Item Option#####################################
def defineItemOption(entries): #defines the item option, either is alz, or item
    alzCheck = checkEventType(entries);
    if alzCheck: #in case its alz, option is quanitty of Alz
        itemOption = int(entries['itemName'].split('[')[1].split(']')[0]);
        if itemOption >= 2147483647:
            itemOption = checkOptionSize(itemOption);
    else: #in case is an item, option is retrieved from column value
        itemOption = int(entries['itemOption'].split('[')[1].split(']')[0]);

    return itemOption;
#########################Check Option Size#####################################
def checkOptionSize(itemOption): # if there is more than PB can take in alz, divide the number of potion of luck
    limit = 2000000000;
    numDiv = math.ceil(itemOption/limit)
    newItemOption = [];
    for i in range(0, numDiv):
        if i == numDiv-1:
            newItemOption.append(itemOption-limit*(numDiv-1))
        else:
            newItemOption.append(2000000000)

    return newItemOption;

#########################Write file Entry #######################################
def restoFileEntries(row):
    entries = defineEntries(row, 'restoFile')
    itemOption = defineItemOption(entries);
    itemKind = getItemKind(entries)
    itemPeriod = getItemPeriod(entries);

    try:# in case the itemOption has more than one entry
        for entry in itemOption:
            string = '<itemServerData itemKind="%d"  itemOption="%d" itemPeriod="%d" />' % (itemKind, entry, itemPeriod);
            print(string)
    except: #item option just with one entry
        string = '<itemServerData itemKind="%d"  itemOption="%d" itemPeriod="%d" />' % (itemKind, itemOption, itemPeriod);

    return string;
#########################Write file Entry ######################################
def getItemName(row):
    entries = defineEntries(row, 'itemsName')
    try:
        itemName = entries['itemName'].split('[')[2].split(']')[0];
    except:
        itemName = "Potion of Luck: " + entries['itemName'].split('[')[1].split(']')[0]  + " Alz";
    return itemName;

#########################Write Output File######################################
def WritePBitemFile(reader, filename):
         with open((filename +".item"),"w+") as filePB:
             with open((filename + ".output"),"w+") as fileTicketAnswer:
                 filePB.write('<?xml version="1.0"?>\n<root>\n')
                 for row in reader:
                     string = restoFileEntries(row);
                     nameString = getItemName(row);

                     filePB.write(string)
                     filePB.write('\n')

                     fileTicketAnswer.write(nameString)
                     fileTicketAnswer.write('\n')

                 filePB.write('</root>')
