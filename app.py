from flask import Flask, render_template, request
from functions import search_for_letters

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Main page')


@app.route('/search-for-letters')
def do_search():
    return render_template('entry.html', title='Search for letters')


@app.route('/results', methods=['POST'])
def search_result():
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase, letters))

    return render_template('result.html', title='Results of searching...',
                           phrase=phrase, letters=letters, results=results)


if __name__ == '__main__':
    app.run(debug=True)
