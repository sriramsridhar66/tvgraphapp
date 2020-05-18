from flask import Flask, request, render_template
from imdb import IMDb

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('landing.html')


@app.route('/', methods=['POST'])
def display_stats():
    text = request.form['showname']
    return print_results(text)


# check if input is an actual tv show, if not tell user, if it is, show graphs

def print_results(search):
    search = IMDb().search_movie(search + ' tv')
    # for movie in search:
    # print(movie)
    series = search[0]
    try:
        IMDb().update(series, 'episodes')
        to_return = ''
        for season_nr in sorted(series['episodes']):
            for episode_nr in sorted(series['episodes'][season_nr]):
                episode = series['episodes'][season_nr][episode_nr]
                to_return += ('Episode ' + str(season_nr) + '.' + str(episode_nr) + ': ' + episode.get(
                    'title') + ' - rating: ' + str(episode.get('rating'))) + '\n'
    except:
        to_return = "Cannot get episodes, searched title is a " + series['kind']
    return to_return


if __name__ == '__main__':
    app.run(debug=True)
