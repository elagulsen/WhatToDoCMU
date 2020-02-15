import flask
#import bridgescrape
from flask import Flask, render_template,request, jsonify

app = Flask(__name__)

#-----------FLASK APPLICATION---------------


#THIS IS THE APPLICATION OBJECT, ALLOWING USE OF APP
app = Flask(__name__)
app.config["DEBUG"] = True #DEBUGGER



#DECORATORS: THEY LINK FUNCTION TO A URL

@app.route('/')
def index():

    return render_template('index.html', title = "Welcome", paragraph = 'Lorem ipsum dolor sit amet')

@app.route('/calendar')
def calendar():
    return render_template('/examples/google-calendar.html')
@app.route('/recommendations')
def recommendations():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('index.html')
if __name__ == 'main':
    app.run()
