import plotly
from imdb import IMDb

import plotly.graph_objects as go

import json


def get_series(search):
    search_add_on = ' tv'
    if search == 'the boys':
        search_add_on = ''
    search_results = IMDb().search_movie(search + search_add_on)
    return search_results[0]


def create_chart(series):
    try:
        IMDb().update(series, 'episodes')
        to_return = ''
        fig = go.Figure()
        for season_nr in sorted(series['episodes']):
            x = []
            y = []
            titles = []
            for episode_nr in sorted(series['episodes'][season_nr]):
                episode = series['episodes'][season_nr][episode_nr]

                x.append(episode_nr)
                y.append(episode.get('rating'))
                titles.append((episode.get('title')))

            if x[0] is None or y[0] is None:
                break
            fig.add_trace(go.Scatter(x=x, y=y, name=f'Season {season_nr}',
                                     line=dict(color=get_random_color(), width=4),
                                     hovertemplate='Episode %{x}:' + '<br><b>''%{text}''</b>' + '<br>Rating: %{y:.2f}',
                                     text=['{}'.format(titles[i]) for i in range(len(x))]))

        fig.update_layout(
            #plot_bgcolor='#7f7f7f',
            #legend_bgcolor='#7f7f7f',
            xaxis_title='Episode',
            yaxis_title='Rating',
            yaxis=dict(
                range=[0, 10],
                dtick=1
            ),
            xaxis=dict(
                tick0=1,
                dtick=1
            )
        )

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

    except Exception as e:
        return str(e)


def get_random_color():
    import matplotlib, random

    hex_colors_dic = {}
    rgb_colors_dic = {}
    hex_colors_only = []
    for name, hex in matplotlib.colors.cnames.items():
        hex_colors_only.append(hex)
        hex_colors_dic[name] = hex
        rgb_colors_dic[name] = matplotlib.colors.to_rgb(hex)

    return random.choice(hex_colors_only)
