from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('landing.html')


@app.route('/', methods=['POST'])
def check_search():
    text = request.form['showname']
    return text

# check if input is an actual tv show, if not tell user, if it is, show graphs


if __name__ == '__main__':
    app.run(debug=True)
