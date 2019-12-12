from flask_api import FlaskAPI
# import flask
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
    print('Done with SQL')
    mes = "test sql"
    return mes


# $dbname = "tantrix5_CompBase"


if __name__ == '__main__':
    app.run(debug=True)
