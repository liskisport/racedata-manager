from builtins import str

from flask_api import FlaskAPI
from flask import jsonify
import mysql.connector
import serial
import time


app = FlaskAPI(__name__)


@app.route('/')
def examaple():
    return 'hello'


@app.route('/com')
def com_read():
    ser = serial.Serial('COM3', bytesize=8, parity='N', stopbits=1)
    ser.write(b' serial port loop test')
    time.sleep(.2)
    if ser.in_waiting > 0:
        serial_line = ser.read(size=ser.in_waiting)
        print(serial_line.decode("utf-8"))
        return 'COM3: ' + serial_line.decode("utf-8")
    else:
        return 'COM3: No Data Available'


@app.route('/res/<int:id>')
def get_comp_results(id):
    mydb = mysql.connector.connect(
        host="80.78.250.41",
        user="tantrix5_root",
        password="Daliluni5",
        database="tantrix5_CompBase"
    )

    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT results.SkierID, Bib, Fname, Name1, SexID, DOB, RunFg1, Res1, RunFg2, Res2, Res1+Res2 AS ResTot FROM results JOIN skiers ON results.SkierID = skiers.SkierID WHERE CompID="+str(id)+" ORDER BY RunFg1, RunFg2, ResTot")
    myresult = mycursor.fetchall()
    for row in myresult:
        for data in row:
            row[data] = str(row[data])

    return jsonify(myresult)


if __name__ == '__main__':
    app.run(debug=True)
