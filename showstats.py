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
        overlay_fig = go.Figure()
        sequential_fig = go.Figure()

        sequential_counter = 0
        sequential_x = []

        for season_nr in sorted(series['episodes']):

            overlay_x = []
            overlay_y = []
            titles = []

            for episode_nr in sorted(series['episodes'][season_nr]):
                episode = series['episodes'][season_nr][episode_nr]

                overlay_x.append(episode_nr)
                overlay_y.append(episode.get('rating'))
                titles.append((episode.get('title')))
                sequential_counter += 1
                sequential_x.append(sequential_counter)

            if season_nr < 0:
                continue
            if overlay_x[0] is None or overlay_y[0] is None:
                break
            color = get_random_color()
            overlay_fig.add_trace(go.Scatter(x=overlay_x, y=overlay_y, name=f'Season {season_nr}',
                                             line=dict(color=color, width=4),
                                             hovertemplate='Episode %{x}:' + '<br><b>''%{text}''</b>' + '<br>Rating: %{y:.2f}',
                                             text=['{}'.format(titles[i]) for i in range(len(overlay_x))]))
            sequential_fig.add_trace(go.Scatter(x=sequential_x, y=overlay_y, name=f'Season {season_nr}',
                                             line=dict(color=color, width=4),
                                             hovertemplate='Episode %{x}:' + '<br><b>''%{text}''</b>' + '<br>Rating: %{y:.2f}',
                                             text=['{}'.format(titles[i]) for i in range(len(overlay_x))]))
            sequential_x.clear()

        overlay_fig.update_layout(
            title='Episode vs Rating Overlaid (Autoscaled)',
            xaxis_title='Episode',
            yaxis_title='Rating',
            xaxis=dict(
                tick0=1,
                dtick=1
            )
        )

        sequential_fig.update_layout(
            title='Episode vs Rating Sequentially',
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

        overlay_graph_JSON = json.dumps(overlay_fig, cls=plotly.utils.PlotlyJSONEncoder)
        sequential_graph_JSON = json.dumps(sequential_fig, cls=plotly.utils.PlotlyJSONEncoder)
        return overlay_graph_JSON, sequential_graph_JSON

    except Exception as e:
        print(str(e))
        return str(e)


def get_random_color(min_v=0.3, max_v=1.0):
    import numpy as np
    from matplotlib.colors import hsv_to_rgb, to_hex

    hsv = np.concatenate([np.random.rand(2), np.random.uniform(min_v, max_v, size=1)])
    return to_hex(hsv_to_rgb(hsv))
