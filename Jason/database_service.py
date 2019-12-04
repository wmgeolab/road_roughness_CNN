import sqlite3
import json
import pandas as pd
from sqlite3 import Error
from sqlite3 import IntegrityError

# Database filepath
file = r"sqlite_database.db"

# Opens a connection to the db file (with given filepath)
def create_connection(file_path):
  conn = None
  try:
    conn = sqlite3.connect(file_path)
    return conn
  except Error as e:
    print(e)
  return conn

# Creates a table
def create_table(conn, sql):
  try:
    c = conn.cursor()
    c.execute(sql)
  except Error as e:
    print(e)

# Inserts into table main
def insert_row_main(conn, data):
  sql = '''INSERT INTO main(uuid, line, distance, iriXp, iriYp, iriZp, iriX, iriY, iriZ)
           VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)'''
  cur = conn.cursor()
  try:
    cur.execute(sql, data)
    conn.commit()
    return ("Successfully inserted with ID of " + str(cur.lastrowid))
  except IntegrityError:
    return ("Failed to Insert!  Duplicate ID or UUID")
  



# Initial setup and testing
def setUp():
  conn = create_connection(file)
  
  create_table_sql = """CREATE TABLE IF NOT EXISTS main (
                      id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                      uuid text UNIQUE,
                      line text,
                      distance real,
                      iriXp real,
                      iriYp real,
                      iriZp real,
                      iriX real,
                      iriY real,
                      iriZ real,
                      filepath text
                      );"""
  
  if conn is not None:
    create_table(conn, create_table_sql)
  else:
    print("Error establishing database connection")   
  conn.close()

  


# Primary function we will receive data into
# Function will parse the data and insert it into the table
def receive_data(args):
  setUp()
  geojsonstring = json.loads(args['geojson_string'])
  line = str(geojsonstring['features'][0]['geometry'])
  properties = geojsonstring['features'][0]['properties']
  uuid = properties['ID']
  distance = properties['DISTANCE']
  iriXp = properties['IRIphoneX']
  iriYp = properties['IRIphoneY']
  iriZp = properties['IRIphoneZ']
  iriX = properties['IRIearthX']
  iriY = properties['IRIearthY']
  iriZ = properties['IRIearthZ']
  conn = create_connection(file)
  data = (uuid, line, distance, iriXp, iriYp, iriZp, iriX, iriY, iriZ)
  print(insert_row_main(conn, data))
  conn.commit()
  df = pd.read_sql_query("SELECT * FROM main", conn)
  conn.close()
  out = df.to_json()
  print(out)
  return out
# Function to retrieve entire SQLite database
def pull_database(args):
  with open('sqlite_database.db', encoding='latin-1') as db:
    content = db.read()
    return content

# main for testing and initial setup
#if __name__ == "__main__":
  #print(pull_database("{}"))
  #pass

  """json=json.loads('''
             {
"type": "FeatureCollection",
"features": [{
"type": "Feature",
"geometry": {
"type": "LineString",
"coordinates": [
[-1.1269799999999999, 50.846999999999994],
[-1.1271983333333333, 50.846898333333336],
[-1.1271983333333333, 50.846898333333336]
]
},
"properties": {
  "ID" : "6",
  "DISTANCE": 19.088285446166992,
  "IRIphoneX": 1.0692366822212474E-5,
  "IRIphoneY": 8.11299430137234E-6,
  "IRIphoneZ": 1.003151410874503E-4,
  "IRIearthX": 3.7928734090129496E-6,
  "IRIearthY": 1.2502931994028412E-5,
  "IRIearthZ": 1.0031453258592652E-4
}
}]
}''')

  receive_data(json)
  con = sqlite3.connect('sqlite_database.db')
  cursor = con.cursor()
  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  print(cursor.fetchall())
  con.close()"""
  #setUp()
  #inp = {'geojson_string': '{"type": "FeatureCollection", "features": [{"type": "Feature", "geometry":{ "type": "LineString","coordinates":[[-1.1600683333333333, 50.85130000000001], [-1.16318, 50.85189999999999], [-1.1639599999999999, 50.85199833333333]]},"properties": {"ID":"55bf58dc-888b-4375-825f-456b8125efc2","DISTANCE":285.0750732421875,"IRIphoneX":7.362987247776638E-7,"IRIphoneY":5.998544784218528E-7,"IRIphoneZ":7.68964295945704E-6,"IRIearthX":7.715770660287904E-7,"IRIearthY":5.506731426280214E-7,"IRIearthZ":7.689602639038619E-6}}]}'}
  #receive_data(inp)

  '''
c = sqlite3.connect(file)
for row in c.execute('SELECT * FROM main'):
    print(row)
c.close()

cnx = sqlite3.connect(file)

df = pd.read_sql_query("SELECT * FROM main", cnx)
df

cnx.close()'''
