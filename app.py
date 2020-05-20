from flask import Flask, request, render_template
from imdb import IMDb

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('landing.html')


@app.route('/', methods=['POST'])
def display_stats():
    text = request.form['showname']
    from showstats import print_results
    return print_results(text)


# check if input is an actual tv show, if not tell user, if it is, show graphs



if __name__ == '__main__':
    app.run(debug=True)
