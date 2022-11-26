import json

def uploadMetadados():
    file = None
    output = None
    try:
        file = open('C:\metadado.json')
        output = json.load(file)['INITIAL']
        file.close()
    except:
        print('Error loading file "metadato"!')
        exit()

    return list(zip(output['id'], output['A'], output['B']))