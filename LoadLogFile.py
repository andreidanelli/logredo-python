# Este pacote é para ler o arquivo de trás para frente linha por linha como unicode de maneira eficiente
from file_read_backwards import FileReadBackwards
# Regular expression operations
import re
# Archives Constants
from Constants import Constants


def loadLogFile():
    global FActionCheckpoint # Validates whether a checkpoint was performed on the current object
    FActionCheckpoint     = False

    global FListRedo         # Transactions to be performed redo 
    FListRedo             = set()   

    global FListOpened       # Transactions without commits
    FListOpened           = set()

    global FListReturn       # Transactions to be updated the new values
    FListReturn           = list()

    try:
        with FileReadBackwards(Constants.DIRECTORY_ARCHIVE_LOG, encoding='utf-8') as frb:
            # Read last record file
            for line in frb:

                # Else if exists Operation Start in current line
                if (re.match(Constants.STRING_START, line)):
                    current_transaction = removeString(Constants.STRING_START_REMOVE, line)
                    actionStart(current_transaction) 

                # If exists commit in current line
                elif (re.match(Constants.STRING_COMMIT, line)):
                    current_transaction = removeString(Constants.STRING_COMMIT_REMOVE, line)
                    actionCommit(current_transaction)
                
                # Else if exists Checkpoint in current line
                elif (re.match(Constants.STRING_CHECKPOINT, line)):
                    current_transaction = removeString(Constants.STRING_CHECKPOINT_REMOVE, line)
                    actionCheckpoint(current_transaction)

                # Else if exists values in current line
                elif (re.match(Constants.STRING_VALUES, line)):
                    current_transaction = removeString(Constants.STRING_VALUES_REMOVE, line)
                    actionValuesLine(current_transaction)

                # Checks if there is checkpoint and no transaction to be done redo
                if (FActionCheckpoint and not FListRedo):
                    return FListReturn

    except Exception as Error:
        print('Unable to read log file!')
        exit()
    finally:
        FListRedo.clear()
        FListOpened.clear()
        frb.close()

    return FListReturn

# Function Start
def actionStart(current_transaction):
    FListOpened.discard(current_transaction)

# Function Commit
def actionCommit(current_transaction):
    if (FActionCheckpoint == False or current_transaction in FListRedo):
        FListOpened.add(current_transaction)

# Function Checkpoint
def actionCheckpoint(current_transaction):
    global FActionCheckpoint
    global FListRedo
    
    FActionCheckpoint = True
    FListRedo = set(current_transaction.split(','))

def actionValuesLine(current_transaction):
    # Add values ​​to vetor
    current_transaction = current_transaction.split(',')
    vetor = []
    vetor = current_transaction
    verifyActionUpdate(vetor)

def verifyActionUpdate(vetor):
    # If the transaction is open, add values ​​to update.
    # If not there was Checkpoint
    if (vetor[0] in FListRedo or not FActionCheckpoint and (vetor[0] in FListOpened)):
        list = {   
                'FTransaction': vetor[0],
                'FId'         : vetor[1],
                'FColumn'     : vetor[2],
                'FOldValue'   : vetor[3],
                'FNewValue'   : vetor[4]
                }
        FListReturn.append(list)

def removeString(String, line):
    line_replace = re.sub(String, '', line).strip()
    return line_replace