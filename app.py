from flask_api import FlaskAPI

import mysql.connector

app = FlaskAPI(__name__)


@app.route('/')
# def examaple():
#    return 'hello'

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

    mycursor.execute("SELECT * FROM results WHERE CompID = 4")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    print('Done with SQL')
    mes = "test sql"
    return mes


# $dbname = "tantrix5_CompBase"


if __name__ == '__main__':
    app.run(debug=True)
