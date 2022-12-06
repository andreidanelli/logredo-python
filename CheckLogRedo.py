# Import log file
from LoadLogFile import loadLogFile
# Archives Constants
from Constants import Constants

import Database

def checkLogRedo():
    try:
        global FTransactions
        FTransactions = dict()

        ListLog = loadLogFile()
        for row in ListLog:
            checkRecordInconsistency(row)
    finally:
        ListLog.clear
        return FTransactions

def checkRecordInconsistency(line_current):
    try:
        FTransaction  = line_current['FTransaction']
        FId           = int(line_current['FId'])
        FColumn       = line_current['FColumn']    
        FNewValue     = int(line_current['FNewValue'])

        if (FTransaction not in FTransactions):
            FTransactions[FTransaction] = 'not_redo'

        SQL = f'SELECT {FColumn} FROM t_logredo WHERE ID = {FId}'

        return_SQL = Database.connectionDatabase(SQL)

        if (return_SQL[0][0] != FNewValue):
            Database.commandUpdate(FId, FColumn, FNewValue)
            # Mark the transactions that were made redo
            FTransactions[FTransaction] = 'redo'
    except:
        print(f'Error checking and updating inconsistency record: {FId}')
        exit()
    finally:
        return FTransactions
        

if __name__ == '__main__':
    checkLogRedo()