from flask_api import FlaskAPI
from flask import jsonify
import mysql.connector

app = FlaskAPI(__name__)


@app.route('/')
def examaple():
    return 'hello'


@app.route('/res')
def get_comp_results():
    print('Start with SQL')
    mydb = mysql.connector.connect(
        host="80.78.250.41",
        user="tantrix5_root",
        password="Daliluni5",
        database="tantrix5_CompBase"
    )

    print(mydb)
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM results WHERE CompID = 1")
    myresult = mycursor.fetchone()
    return jsonify(name='skier', dob='old')


if __name__ == '__main__':
    app.run(debug=True)
