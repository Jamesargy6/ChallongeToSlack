import json

def loadJsonFile(fileLoc, mode):

	file = open(fileLoc, mode)
	raw_json = file.read()
	parsed_json = json.loads(raw_json)

	return parsed_json

def dumpJson(fileLoc, data):
	file = open(fileLoc, "w")
	json.dump(data, file)
