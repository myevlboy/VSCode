from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add this line

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        session['user_input'] = request.form.get('user_input')
        return redirect(url_for('hello_world'))
    user_input = session.get('user_input')
    return render_template('MainPage.html', user_input=user_input)

@app.route('/second')
def second_page():
    return render_template('SecondPage.html')

@app.route('/input', methods=['GET', 'POST'])
def User_Input():
    if request.method == 'POST':
        session['user_input'] = request.form.get('user_input')
        return redirect(url_for('User_Input'))
    user_input = session.get('user_input')
    return render_template('UserInput.html', user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)