import csv
from lib.defineEntries import defineEntries


##########################Defines Config for TSV file###########################
def getDungeonEntries(row):
    entries = defineEntries(row, 'dungeon')
    event = entries['event']

    try:
        return {
            'DungeonEnter': {'event': entries['event'],
                            'dungeon' : entries['dungeon'].split('[')[2].split(']')[0],
                            'date' : entries['date'],
                            'time' : entries['time'],
                            },

            'DungeonExit': {'event': entries['event'],
                            'dungeon' : entries['dungeon'].split('[')[2].split(']')[0],
                            'date' : entries['date'],
                            'time' : entries['time'],
                            'exitCondition' : entries['exitCondition'].split('[')[1].split(']')[0],
                            },

            'DungeonRewardInformation': {'event': entries['event'],
                                        'dungeon' : entries['dungeon'].split('[')[2].split(']')[0],
                                        'date' : entries['date'],
                                        'time' : entries['time'],
                                        'clearCount' : entries['clearCount'].split('[')[1].split(']')[0],
                                        },

            'DungeonRewardItem': {'event': entries['event'],
                                'reward' : entries['dungeon'].split('[')[2].split(']')[0],
                                'date' : entries['date'],
                                'time' : entries['time'],
                                },
                }[event]
    except:
        return {}
###############################################################################
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches
###############################################################################
def createDungeonString(string,count,entry,exitCondition,dungeonDataDict):
    if entry['event'] == 'DungeonEnter':
        string +=entry['date'] + ' ' + entry['event']  + ': ' + entry['time'] + ' '


    elif entry['event'] == 'DungeonRewardInformation' and count == 0: #This entry shows twice on log, count makes sure it just gets output once
        string += 'Day Count: ' + entry['clearCount'] + ' '
        count = 1;


    elif entry['event'] == 'DungeonRewardItem':
        string += 'Reward: ' + entry['reward'] + ' '


    elif entry['event'] == 'DungeonExit':
        string += entry['event'] + ': ' + entry['time']  + ' ' + exitCondition[int(entry['exitCondition'])] + ' '
        print(string)

        index = list(find_all(string,'DungeonEnter')) # Find if string has entry without exit

        if entry['dungeon'] in dungeonDataDict: #if data entry already exists, just appends the new entry;
            if len(index) != 1: #if theres double EnterDungeon Entry, separate it in two lines
                for i in range(0,len(index)-1):
                    string1 = string[0:index[i+1]-index[i]-1]
                    string2 = string[index[i+1]-index[i]:-1]
                    dungeonDataDict[entry['dungeon']].append(string1);
                    dungeonDataDict[entry['dungeon']].append(string2);
            else:
                dungeonDataDict[entry['dungeon']].append(string);

        else: #if the dict  does not have that event type, create and then append

            if len(index) != 1: #if theres double EnterDungeon Entry, separate it in two lines
                for i in range(0,len(index)-1):
                    string1 = string[0:index[i+1]-index[i]-1]
                    string2 = string[index[i+1]-index[i]:-1]
                    dungeonDataDict[entry['dungeon']]=[];
                    dungeonDataDict[entry['dungeon']].append(string1);
                    dungeonDataDict[entry['dungeon']].append(string2);
            else:
                dungeonDataDict[entry['dungeon']]=[];
                dungeonDataDict[entry['dungeon']].append(string);

        #Reset Variables
        string = ''
        count = 0;


    return dungeonDataDict

###############################################################################
def getDictDungeonData(reader):
    #Initialize Variables
    string = ''
    count = 0;
    exitCondition = {0:'Success',1:'TimeOut',2:'Dead',3:'Cancel',4:'Giveup',5:'ReleaseParty'}
    dungeonDataDict = {}
    for row in reader:
        entry = getDungeonEntries(row)
        if entry != {}:
            #dungeonDataDict = createDungeonString(string,count,entry,exitCondition,dungeonDataDict)
            if entry['event'] == 'DungeonEnter':
                string +=entry['date'] + ' ' + entry['event']  + ': ' + entry['time'] + ' '


            elif entry['event'] == 'DungeonRewardInformation' and count == 0: #This entry shows twice on log, count makes sure it just gets output once
                string += 'Day Count: ' + entry['clearCount'] + ' '
                count = 1;


            elif entry['event'] == 'DungeonRewardItem':
                string += 'Reward: ' + entry['reward'] + ' '


            elif entry['event'] == 'DungeonExit':
                string += entry['event'] + ': ' + entry['time']  + ' ' + exitCondition[int(entry['exitCondition'])] + ' '

                index = list(find_all(string,'DungeonEnter')) # Find if string has entry without exit

                if entry['dungeon'] in dungeonDataDict: #if data entry already exists, just appends the new entry;
                    if len(index) != 1: #if theres double EnterDungeon Entry, separate it in two lines
                        for i in range(0,len(index)-1):
                            string1 = string[0:index[i+1]-index[i]-1]
                            string2 = string[index[i+1]-index[i]:-1]
                            dungeonDataDict[entry['dungeon']].append(string1);
                            dungeonDataDict[entry['dungeon']].append(string2);
                    else:
                        dungeonDataDict[entry['dungeon']].append(string);

                else: #if the dict  does not have that event type, create and then append

                    if len(index) != 1: #if theres double EnterDungeon Entry, separate it in two lines
                        for i in range(0,len(index)-1):
                            string1 = string[0:index[i+1]-index[i]-1]
                            string2 = string[index[i+1]-index[i]:-1]
                            dungeonDataDict[entry['dungeon']]=[];
                            dungeonDataDict[entry['dungeon']].append(string1);
                            dungeonDataDict[entry['dungeon']].append(string2);
                    else:
                        dungeonDataDict[entry['dungeon']]=[];
                        dungeonDataDict[entry['dungeon']].append(string);

                #Reset Variables
                string = ''
                count = 0;


    return dungeonDataDict



################################################################################
def writeOutputDungeonAnalysis(reader,filename):
    with open(filename + ".output", "w+") as txtfile:
        dungeonDataDict = getDictDungeonData(reader);
        for key,value in dungeonDataDict.items():
            txtfile.write(key + '\n')
            for i in range(0, len(value)):
                txtfile.write(value[i] + '\n')
            txtfile.write('\n')




























            #print(entry)
