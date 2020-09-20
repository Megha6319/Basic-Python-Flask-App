from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
	return '<h1 style="color:#FF0000"><center>The basic Python Flask App</center></h1>'

@app.route('/Instruction')
def Instruction(): 
    return '<h1 style="color:#FF00FF"><center>Instructions and commands on how to install and open the basic Python Flask App</center></h1>'   

@app.route('/Python')
def Python():
	return '<h1 style="color:#4B0082">1.Open command prompt to run commands.</h1>'

@app.route('/Flask')
def Flask():
	return '<h1 style="color:#4B0082">2.Name a folder as flask_app and run (py -m venv env) on command prompt.This installs the env folder.</h1>'

@app.route('/first')
def first():
	return '<h1 style="color:#4B0082">3.Then give (env\ Scripts \ activate)to activate env.</h1>'

@app.route('/flaskapp')
def flaskapp():
	return '<h1 style="color:#4B0082">4.Then type the command (pip install flask) to install flask_app.</h1>'

@app.route('/Basic')
def Basic():
	return '<h1 style="color:#4B0082">5.And (set FLASK_APP=app.py) where app.py is the name to be saved on Sublime text.</h1> '

@app.route('/Tryitout')
def Tryitout():
	return '<h1 style="color:#4B0082">6.Then type the commands on Sublime Text save it,and give (flask run),this gives us the ip address copy ,paste it on a new tab.</h1> '
	
@app.route('/Happylearning')
def Happylearning():
    return '<h1 style="color:#4B0082">7.The first command runs with the same ip address , but for the rest of commands ,by considering the third return command to run copy,paste ip address and give /Python,it should look like (http://127.0.0.1:5000/Python).</h1>  '

if __name__ == "__main__":
	app.run(debug=True)