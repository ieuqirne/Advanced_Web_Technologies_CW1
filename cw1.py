from flask import Flask, render_template, json, request, url_for, redirect, flash
from pprint import pprint
import os

app = Flask(__name__)

@app.route('/')
def root():
    INDEX = os.path.realpath(os.path.dirname(__file__))
    with open(os.path.join(INDEX ,'static', 'data.json')) as f:
        data = json.load (f)
        return render_template('movieInfo.html', data=data),200

#uploading data
@app.route("/uploading/", methods=['POST','GET'])
def uploading():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/img/file.png')
        return "File Uploaded"
    else:
        return render_template('uploading.html')
#year
@app.route("/allmovies/")
def movies():
        INDEX = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(INDEX ,'static', 'data.json')) as f:
            data = json.load (f)
            return render_template('listMovies.html', data=data),200

@app.route("/allmovies/<mov>/")
def movie(mov=None):
    INDEX = os.path.realpath(os.path.dirname(__file__))
    with open(os.path.join(INDEX ,'static', 'data.json')) as f:
        data = json.load (f)
        return render_template('movieInfo.html', data=data, mov=mov),200

@app.route("/allmovies/act/")
def listAct(mov=None):
    INDEX = os.path.realpath(os.path.dirname(__file__))
    with open(os.path.join(INDEX ,'static', 'data.json')) as f:
        data = json.load (f)
        return render_template('listAct.html', data=data, mov=mov),200

@app.route("/allmovies/act/<act>/")
def actInfo(act=None):
    INDEX = os.path.realpath(os.path.dirname(__file__))
    with open(os.path.join(INDEX ,'static', 'data.json')) as f:
        data = json.load (f)
        return render_template('actInfo.html', data=data, act=act),200

@app.route("/allmovies/genre/")
def allGenres(mov=None):
    INDEX = os.path.realpath(os.path.dirname(__file__))
    with open(os.path.join(INDEX ,'static', 'data.json')) as f:
        data = json.load (f)
        return render_template('allGenres.html', data=data),200

@app.route("/allmovies/genre/<genre>/")
def genres(genre=None):
    if(genre == "action" or genre == "adventure" or genre == "comedy" or genre == "crime" or genre == "historical"
    or genre == "drama" or genre == "horror" or genre == "sciencefiction" or genre == "war" or genre == "western"):
        INDEX = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(INDEX ,'static', 'data.json')) as f:
            data = json.load (f)
            return render_template('listMoviesByGenre.html', data=data, genre=genre),200
    else:
        return redirect(url_for('movies'))

@app.route("/allmovies/year/")
def allYears(mov=None):
    INDEX = os.path.realpath(os.path.dirname(__file__))
    with open(os.path.join(INDEX ,'static', 'data.json')) as f:
        data = json.load (f)
        return render_template('allYears.html', data=data),200

@app.route("/allmovies/year/<int:year>/")
def year(year=None):
    if(year<1994 or year>2008):
        return redirect(url_for('movies'))
    else:
        INDEX = os.path.realpath(os.path.dirname(__file__))
        with open(os.path.join(INDEX ,'static', 'data.json')) as f:
            data = json.load (f)
            return render_template('listMoviesByYear.html', data=data, year=year),200


#testing
def init(app):
    config = ConfigParser.ConfigParser()
    try:
        config_location = "etc/logging.cfg"
        config.read(config_location)

        app.config['DEBUG'] = config.get("config","debug")
        app.config['ip_address'] = config.get("config", "ip_address")

        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config","url")

        app.config['log_file'] = config.get("config", "name")
        app.config['log_location'] = config.get("config", "location")
        app.config['log_level'] = config.get("config", "level")
    except:
        print ("Could not read configs from: ", config_location)

def logs(app):
    log_pathname = app.config['log_location'] + app.config['log_file']
    file_handler = RotatingFileHandler(log_pathname, maxBytes=1024*1024*10 , backupCount=1024)
    file_handler.setLevel( app.config['log_level'])
    formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(module)s | %(funcName)s | %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.setLevel( app.config['log_level'])
    app.logger.addHandler(file_handler)

#Working with Errorst
@app.route('/force404')
def force404():
	abort(404)

@app.errorhandler(404)
def page_not_found(error):
    message ="Couldn't find the page you requested"
    return render_template('message.html', message=message), 404

#redirect


if __name__==" __main__ ":
    app.run(host ='0.0.0.0',debug=True)
