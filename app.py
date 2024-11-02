import os
from flask import Flask, render_template, request, send_file
# from PIL import Image
# from io import BytesIO
import services
import json

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_PATH'] = 'uploads'
upload_directory = os.path.join(basedir, app.config['UPLOAD_PATH'])
if not os.path.exists(upload_directory):
    os.makedirs(upload_directory)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400
        if file:
            print("process started")
            file.save(os.path.join(basedir, app.config['UPLOAD_PATH'], file.filename))
            response = services.call_gemini2(os.path.join(basedir, app.config['UPLOAD_PATH'], file.filename))
            print((response))
            output = json.loads(response)
            os.remove(os.path.join(app.config['UPLOAD_PATH'],  file.filename))
            print("process completed")
            return render_template('output.html',summary = output["summary"], positives =  output["positives"], negatives = output["negatives"],tech = output["tech-jargon"] ) 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)