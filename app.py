from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	with open("output.txt") as output_file:
		output_string = output_file.read()
	return render_template('index.html', output_string = output_string)
	if not output_file.closed:
		output_file.close()

if __name__ == "__main__":
	app.run(debug=True,port=5000,host="0.0.0.0")
