# Used to work with JSON data
import json
# Archives Constants
from Constants import Constants


# Archives Constants
from Constants import Constants
def uploadMetadados():
    file = None
    output = None
    try:
        file = open(Constants.DIRECTORY_METADADO)
        output = json.load(file)['INITIAL']
        file.close()
    except:
        print('Error loading file "metadado"!')
        exit()

    return list(zip(output['id'], output['A'], output['B']))