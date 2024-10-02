from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    utc_time = datetime.now(pytz.utc)
    eastern = pytz.timezone('America/New_York')
    eastern_time = utc_time.astimezone(eastern)
    return {'The time is': eastern_time.strftime('%Y-%m-%d %H:%M:%S %Z')}


app.run(host='0.0.0.0',
        port=8080)