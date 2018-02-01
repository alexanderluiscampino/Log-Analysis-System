##################### Define Entries to read from log file #####################
def defineEntries(row, option):
     return {
         'restoFile': {'event': row['column5'],
                       'itemIndex' : row['column6'],
                       'itemName' : row['column8'],
                       'itemOption' : row['column9'],
                       'itemPeriod' : [row['column14'], row['column11'], row['column12']]},

         'itemsName': {'itemName' : row['column8']},

         'IP': {'event': row['column5'],
                'date' : row['column2'],
                'time' : row['column3'],
                'IPAddress' : row['column17']},

        'itemMvmnt': {'event': row['column5'],
                      'itemName' : row['column8'],
                      'date' : row['column2'],
                      'time' : row['column3'],
                      'tradeItem' : row['column11'],
                      'mailItem' : row['column13'],
                      'tradeAlz' : row['column10'],
                      'AgentShop' : [row['column10'], row['column12'], row['column13']], # buyer & price & count
                      'PersonalShop' : [row['column7'], row['column12'], row['column11']], # buyer & price & seller
                      'npcSell': row['column11'],
                      'world' : row['column14']
                      },
        'dungeon': {'event': row['column5'],
                      'dungeon' : row['column8'],
                      'clearCount' : row['column11'],
                      'exitCondition' : row['column12'],
                      'date' : row['column2'],
                      'time' : row['column3'],
                      },
     }[option]
