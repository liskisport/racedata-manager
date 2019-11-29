from flask_api import FlaskAPI
import json

app = FlaskAPI(__name__)


@app.route('/')
def example():
    return 'hello'


@app.route('/competition/<int:id>')
def competition(id):
    with open('./mock/competition_data.json', 'r') as competition_data_file:
        competition_data = competition_data_file.read()

    return json.loads(competition_data)


if __name__ == '__main__':
    app.run(debug=True)
