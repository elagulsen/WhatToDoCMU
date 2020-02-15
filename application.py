import flask
from flask import Flask, render_template,request, jsonify

app = Flask(__name__)

#-----------FLASK APPLICATION---------------


#THIS IS THE APPLICATION OBJECT, ALLOWING USE OF APP
app = Flask(__name__)
app.config["DEBUG"] = True #DEBUGGER



#DECORATORS: THEY LINK FUNCTION TO A URL

@app.route('/')
def hello_world():

    return render_template('index.html', title = "Welcome", paragraph = 'Lorem ipsum dolor sit amet')

if __name__ == 'main':
    app.run()
