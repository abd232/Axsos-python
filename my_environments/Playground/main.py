from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello_world():
    return "hello world!"

@app.route('/play')
def play():
    return render_template("play.html", times=3, color="blue")

@app.route('/play/<times>')
def play_with_times(times):
    return render_template("play.html", times=int(times), color="blue")

@app.route('/play/<times>/<color>')
def play_with_times_and_color(times, color):
    return render_template("play.html", times=int(times), color=color)

if __name__=="__main__":
    app.run(debug=True)  