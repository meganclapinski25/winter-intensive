from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/workoutpage')
def workoutpage():
    return render_template('workoutex.html')


if __name__ == '__main__':
    app.run(debug=True)