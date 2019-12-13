from flask_api import FlaskAPI
from flask import jsonify
import mysql.connector


app = FlaskAPI(__name__)


@app.route('/')
def examaple():
    return 'hello'


@app.route('/res')
def get_comp_results():
    mydb = mysql.connector.connect(
        host="80.78.250.41",
        user="tantrix5_root",
        password="Daliluni5",
        database="tantrix5_CompBase"
    )


    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT results.SkierID, Bib, Fname, Name1, SexID, DOB, RunFg1, Res1, RunFg2, Res2, Res1+Res2 AS ResTot FROM results JOIN skiers ON results.SkierID = skiers.SkierID WHERE CompID=4 ORDER BY RunFg1, RunFg2, ResTot")
    myresult = mycursor.fetchall()
    for row in myresult:
        for data in row:
            row[data] = str(row[data])

    return jsonify(myresult)


if __name__ == '__main__':
    app.run(debug=True)
