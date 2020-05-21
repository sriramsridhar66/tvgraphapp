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
                                     line=dict(color=get_color(), width=4)))

        #fig.update_yaxes(tickvals=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        fig.update_layout(title=f'{str(series)}',
                          xaxis_title='Episode',
                          yaxis_title='Rating',
                          yaxis=dict(
                              range=[0, 10],
                              dtick=1
                          ),
                          xaxis=dict(
                              tickmode='linear',
                              tick0=1,
                              dtick=1
                          )
                          )

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return graphJSON
    except Exception as e:
        return str(e)


def get_color():
    import matplotlib, random

    hex_colors_dic = {}
    rgb_colors_dic = {}
    hex_colors_only = []
    for name, hex in matplotlib.colors.cnames.items():
        hex_colors_only.append(hex)
        hex_colors_dic[name] = hex
        rgb_colors_dic[name] = matplotlib.colors.to_rgb(hex)

    return random.choice(hex_colors_only)
