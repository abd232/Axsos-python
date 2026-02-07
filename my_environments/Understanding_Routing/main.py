from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/Champion')          # The "@" decorator associates this route with the function immediately following
def Champion():
    return 'Champion!'  # Return the string 'Hello World!' as a response

@app.route('/say/<text>')  # The "@" decorator associates this route with the function immediately following
def Say(text):
    return f"Hi {text}!"

@app.route('/repeat/<int:times>/<text>')  # The "@" decorator associates this route with the function immediately following
def repeat(times, text):
    return f"{text} " * times


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
