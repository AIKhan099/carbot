from pathlib import Path
import json
pp=str(Path(__file__).parents[1])+'\static\credentials.json'
pp1=Path(__file__).parent
print(pp,pp1)
# F:\AI\PROJECTS\feb\feb23\new\carbot\static\credentials.json
credentials = open(pp)
cred_json = json.load(credentials)
print(cred_json)