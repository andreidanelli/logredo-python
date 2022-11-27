# Este pacote é para ler o arquivo de trás para frente linha por linha como unicode de maneira eficiente
from file_read_backwards import FileReadBackwards
# Regular expression operations
import re

def loadLogFile():
    try:
        global FActionCheckpoint # Validates whether a checkpoint was performed on the current object
        global FListRedo         # Transactions to be performed redo 
        global FListOpened       # Transactions without commits

        FActionCheckpoint = False
        FListOpened = set()
        FListRedo   = set()   
        
        with FileReadBackwards('C:\entradaLog', encoding='utf-8') as frb:
            # Read last record file
            for line in frb:
                # If exists commit in current line
                if (re.match('^<commit .+>', line)):
                    current_transaction = re.sub('<commit|>', '', line).strip()
                    verifyActionCommit(current_transaction)
                
                # Else if exists Checkpoint in current line
                elif (re.match('^<CKPT\s*\\(.*\\)\s*>', line)):
                    current_transaction = re.sub('^<CKPT\s*\\(.*\\)\s*>', '', line)
                    verifyActionCheckpoint(current_transaction)

    except Exception as Error:
        print('Unable to read log file!')
        exit()

# Function Commit
def verifyActionCommit(current_transaction):
    if (FActionCheckpoint == False or current_transaction in FListRedo):
        FListOpened.add(current_transaction)

# Function Checkpoint
def verifyActionCheckpoint(current_transaction):
    FActionCheckpoint = True

    if current_transaction:
        # Added transaction in list of redo
        FListRedo = set(current_transaction.split(','))
