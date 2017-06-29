from flask import Flask, render_template
import requests
import random

app = Flask(__name__)
app.debug = True

def get_data():
    url = "https://raw.githubusercontent.com/ischurov/dj-prog/master/pushkin1.json"
    r = requests.get(url)
    m = r.json()
    for row in m['poems']:
        if row['title'] == ['* * *']:
            if row['verses'][0] != "":
                row['title'] = row['verses'][0]
            else:
                row['title'] = row['verses'][1]
    return m['poems']

@app.route('/')
def my_page():
    return render_template("my_page.html",
                           data=get_data())

@app.route('/poem/<int:n>')
def show_poem(n):
    n = n-1
    data = get_data()
    row = data[n]
    return render_template("show_poem.html",
                           row=row, n=n+1)
@app.route('/random')
def random_poem ():
    data = get_data()
    random_poems = random.choice(data)
    return render_template("random_poem.html",
                           row=random_poems)


if __name__ == '__main__':
    app.run()