from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def homepage():
	return render_template('index.html')


if __name__ == "__main__":
	app.config['TEMPLATES_AUTO_RELOAD']=True
	app.config['DEBUG'] = True
	app.config['SERVER_NAME'] = "127.0.0.1:5000"         
	app.run()