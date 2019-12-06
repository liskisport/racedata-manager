from flask import jsonify
from flask_api import FlaskAPI
import json
import mysql.connector



app = FlaskAPI(__name__)

#with open('./tmp/competition_data.json', 'r') as competition_data_file:
#    competition_data = competition_data_file.read()


@app.route('/')
def example():
    return 'hello'


@app.route('/competition/<int:id>')
mydb = mysql.connector.connect(
  host="tantriks.ru",
  user="Jora",
  passwd="daliluni"
)

mycursor = mydb.cursor()

def competition(id):
    return jsonify(json.loads(competition_data))


if __name__ == '__main__':
    app.run(debug=True)
