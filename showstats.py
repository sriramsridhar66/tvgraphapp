import plotly
from imdb import IMDb

import plotly.graph_objects as go

import json


def create_chart(search):
    search = IMDb().search_movie(search + ' tv')
    # for movie in search:
    # print(movie)
    series = search[0]
    try:
        IMDb().update(series, 'episodes')
        to_return = ''
        fig = go.Figure()
        for season_nr in sorted(series['episodes']):
            x = []
            y = []
            for episode_nr in sorted(series['episodes'][season_nr]):
                episode = series['episodes'][season_nr][episode_nr]

                x.append(episode_nr)
                y.append(episode.get('rating'))

                # to_return += ('Episode ' + str(season_nr) + '.' + str(episode_nr) + ': ' + episode.get(
                # 'title') + ' - rating: ' + str(episode.get('rating'))) + '\n'
        fig.add_trace(go.Scatter(x=x, y=y, name=f'Season {season_nr}',
                                 line=dict(color='firebrick', width=4)))

        fig.update_layout(title=f'{str(series)}',
                          xaxis_title='Episode',
                          yaxis_title='Rating')
        fig.show()
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return graphJSON
    except:
        return "Cannot get episodes, searched title is a " + series['kind']
