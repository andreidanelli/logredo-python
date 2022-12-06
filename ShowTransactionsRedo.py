from CheckLogRedo import checkLogRedo
# Show values JSON
from Database import connectionDatabase
# Library Json
import json
# Archives Constants
from Constants import Constants

def showTransactionsRedo():

    listRedo = checkLogRedo();

    for redo in listRedo:
        if listRedo[redo]:
            print(f'Transação {redo} realizou Redo')
            continue
        print('Transação {redo} não realizou Redo')

    showJsonInitial()
    showJsonFinal()

def showJsonInitial():
    with open(Constants.DIRECTORY_METADADO, 'r') as openfile:
        json_object = json.load(openfile)
        print(json_object)

def showJsonFinal():
   json_object = dict()
   return_SQL = connectionDatabase(Constants.SELECT_REGISTERS)

   for line in return_SQL:
    json_object['ID'] = line[0]
    json_object['A'] = line[1]
    json_object['B'] = line[2]

    print(json_object)

