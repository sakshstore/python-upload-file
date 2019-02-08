import os
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return 'Index Page'

 

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join("uploads", file.filename)
    
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    file.save(f)

    return render_template('index.html')
	
	
@app.route('/send')
def hello_world():
    return render_template('index.html')