import json

def json_file_write(filename, dictionary):
    jsonString = json.dumps(dictionary)
    jsonFile = open(filename, "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    print('\n', 'json_file was saved to: ', filename, '\n')


def json_file_read(filename):
    with open(filename) as json_data:
        d = json.load(json_data)
        json_data.close()
    return d
    