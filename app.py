from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def Profile():
	return render_template('faiza.html')
	
@app.route('/Place')
def Place():
	return 'Hello from Github repo'
app.run()
