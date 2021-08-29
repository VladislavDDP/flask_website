from os import sep
from flask import Flask, render_template, request, escape

app = Flask(__name__)


def search_for_letters(phrase: str, letters: str) -> set: 
    return set(letters).intersection(set(phrase))


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/viewlog')
def view_log():
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))

    column_titles = ('Form data', 'Remote address', 'User Agent', 'Results')
    return render_template('viewlog.html',  the_title='View logs',
                                            the_column_titles=column_titles,
                                            the_contents=contents)


@app.route('/')
def index():
    return render_template('index.html', the_title='Main page')


@app.route('/search-for-letters')
def do_search():
    return render_template('entry.html', the_title='Search for letters')


@app.route('/results', methods=['POST'])
def search_result():
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase, letters))
    log_request(request, results)
    return render_template('result.html', the_title='Results of searching...',
                           phrase=phrase, letters=letters, results=results)


if __name__ == '__main__':
    app.run(debug=True)
