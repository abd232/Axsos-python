from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')
def home():
    if 'visited_time' in session:
        session['visited_time'] = session.get('visited_time') + 1
    else:
        session['visited_time'] = 1
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('index.html')
    
@app.route('/incrementbytwo')
def increment_by_two():
    if 'counter' in session:
        session['counter'] = session.get('counter') + 2
    else:
        session['counter'] = 2
    return render_template('index.html')

@app.route('/increment', methods=['POST'])

def increment():
    increment_value = int(request.form.get('increment_value'))  # Default to 1 if not provided
    if 'counter' in session:
        session['counter'] = session.get('counter') + increment_value
    else:
        session['counter'] = increment_value
    return render_template('index.html')

@app.route('/reset')
def reset():
    session['counter'] = 0
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')
    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.