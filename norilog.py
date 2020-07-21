import json

from flask import Flask, render_template

app = Flask(__name__)

DATA_FILE = "norilog.json"

def save_data(start, finish, memo, created_at):
    """ store data posted
    :param start: station rode on
    :type start: str
    :param finish: station rode off
    :type finish: str
    :param memo: memorandom for purporse
    :type memo: str
    :param created_at: datetime when used train
    :type created_at: datetime.datetime
    :return: None
    """
    
    try:
        # open database file with json module
        database = json.load(open(DATA_FILE, mode='r', encoding="utf-8"))
    except FileNotFoundError:
        database = []
        
    database.insert(0, {
        "start": start,
        "finish": finish,
        "memo": memo,
        "created_at": created_at.strftime("%Y-%m-%d %h:%M")
    })
    json.dump(database, open(DATA_FILE, mode='w', encoding="utf-8"), indent=4, ensure_ascii=False)

def load_data():
    """return stored json-data"""
    try:
        # open database file with json module
        database = json.load(open(DATA_FILE, mode='r', encoding="utf-8"))
    except FileNotFoundError:
        database = []
        
    return database

@app.route('/')
def index():
    """ Top page
    rendering the top page using render_template
    """
    return render_template('index.html')


if __name__ == '__main__':
    # execute app by 0.0.0.0:8000
    app.run('0.0.0.0', 8000, debug=True)

