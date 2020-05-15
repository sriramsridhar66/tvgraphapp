from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return """
         <html><body>
             <h2>Test Home Page</h2>
             <form action="/test">
                 Enter TV series <input type='text' name='showname'>
                 <input type='submit' value='Search and Plot'>
             </form>
         </body></html>
         """


@app.route('/test')
def test():
    return 'test'


if __name__ == '__main__':
    app.run(debug=True)
