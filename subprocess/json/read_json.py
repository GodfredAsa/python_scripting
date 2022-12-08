import json


req_file = "subprocess\json\data.json"

f = open(req_file, 'r')

data = json.load(f)

title = data["glossary"]["title"]

f.close()
