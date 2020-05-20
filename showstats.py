from imdb import IMDb

import plotly
import plotly.graph_objs as go

import json


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
