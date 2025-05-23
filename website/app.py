from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('MainPage.html')
#second page
@app.route('/second')
def second_page():
    return render_template('SecondPage.html')

if __name__ == '__main__':
    app.run(debug=True)