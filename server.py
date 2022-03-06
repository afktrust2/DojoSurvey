from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'test key 2'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def user_inputs():
    print("User input:")
    print(request.form)
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['fav_lang'] = request.form['lang']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def reset():
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True, host='localhost', port=3306)