from flask import Flask, render_template
app = Flask(__name__)   

@app.route('/')         
def index():
    return render_template("index.html", x=8, y=8,color1="black", color2="red")  

@app.route('/<x>')
def index_x(x):
    return render_template("index.html", x=int(x), y=8,color1="black", color2="red")

@app.route('/<x>/<y>')
def index_xy(x,y):
    return render_template("index.html", x=int(x), y=int(y),color1="black", color2="red")

@app.route('/<x>/<y>/<color1>/<color2>')    
def index_xyc(x,y,color1,color2):
    return render_template("index.html", x=int(x), y=int(y),color1=color1, color2=color2)

if __name__=="__main__":   
    app.run(debug=True)