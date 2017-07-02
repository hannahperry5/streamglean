from flask import Flask
from flask import render_template
from application import db
from application.models import Data

import datetime
import requests


# Create the Flask app
application = Flask(__name__)
application.debug = True


# print a nice greeting.

# print a nice greeting.
@application.route('/')
def say_hello():
    json = requests.get('https://api.twitch.tv/kraken/communities/top', headers=headers).json()
    top['communities'] = json['communities']
    json = requests.get('https://api.twitch.tv/kraken/games/top', headers=headers).json()
    top['games'] = json['top']
    json = requests.get('https://api.twitch.tv/kraken/streams', headers=headers).json()
    channels = json['streams']
    top['channels'] = channels
    return render_template('index2.html', name=top)

@application.route('/games/league-of-legends')
def show_league_of_legends():
    return render_template('league-of-legends.html')

@application.route('/games/dota-2')
def show_dota_2():
    return render_template('dota-2.html')

@application.route('/games/counter-strike-global-offensive')
def show_counter_strike():
    return render_template('counter-strike-global-offensive.html')

@application.route('/streamers/LegendaryLea')
def show_legendary_lea():
    return render_template('LegendaryLea.html')

@application.route('/streamers/LIRIK')
def show_lirik():
    return render_template('LIRIK.html')

@application.route('/streamers/MitchJones')
def show_mitch():
    return render_template('MitchJones.html')

@application.route('/communities/positivity')
def show_positivity():
    return render_template('positivity.html')

@application.route('/communities/speedrunning')
def show_speedrunning():
    return render_template('speedrunning.html')

@application.route('/communities/catsonly')
def show_catsonly():
    return render_template('catsonly.html')

@application.route('/teams/tempostorm')
def show_tempostorm():
    return render_template('tempostorm.html')

@application.route('/teams/gfe')
def show_gfe():
    return render_template('gfe.html')

@application.route('/teams/cloud9')
def show_cloud9():
    return render_template('cloud9.html')


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    application.run()