#from flask import jsonify
from flask_api import FlaskAPI
from flask_mysqldb import MySQL
from envparse import env
#import json
#import mysql.connector

app = FlaskAPI(__name__)

@app.route('/')
def example():
    return 'hello'


@app.route('/competition/<int:id>')
# Configure MySQL
app.config['MYSQL_HOST'] = env('tantriks.ru', cast=str)
app.config['MYSQL_USER'] = env('tantrix5_root', cast=str)
app.config['MYSQL_PASSWORD'] = env('Daliluni5', cast=str)
app.config['MYSQL_DB'] = env('tantrix5_CompBase', cast=str)
app.config['MYSQL_CURSORCLASS'] = 'CompCursor'

# Initialise MySQL
mysql = MySQL(app)


CompCursor.execute('SELECT * FROM results WHERE CompID = id')
comp_results = CompCursor.fetchall()

for x in comp_results:
  print(x)

#def competition(id):
#    return jsonify(json.loads(competition_data))


if __name__ == '__main__':
    app.run(debug=True)
