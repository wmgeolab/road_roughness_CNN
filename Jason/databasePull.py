import requests
import json as json
import sqlite3

r = requests.post('https://cdsw.geo.sciclone.wm.edu/api/altus-ds-1/models/call-model', data='{"accessKey":"m81pey3nzvnbzjzoac0pp47n2jobjqeq","request":{"param":"value"}}', headers={'Content-Type': 'application/json'}, verify=False)

db = json.loads(r.content)


con = sqlite3.connect('data.db')
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
con.close()

with open("data.db","w+") as file:
  file.write(db['response'])