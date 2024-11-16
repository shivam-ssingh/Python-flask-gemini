import os
from flask import Flask, jsonify, render_template, request, send_file
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
            # response = response.replace('json ', '')
            print('response is:')
            print((response.strip()))
            print("Raw response:", repr(response))
            print("Response type:", type(response))
            print("Response length:", len(response))
            response = response.strip('```json\n').strip()
            # if not response.strip():
            #     return jsonify({"error": "Empty response from generate_content"}), 500
            # try:
            #     output = json.loads(response.strip())
            # except json.JSONDecodeError as e:
            #     print("JSON Decode Error:", str(e))
            #     print("Response content:", response)
            #     return jsonify({"error": "Invalid JSON response"}), 500
            output = json.loads(response.strip())
            print(output)
            os.remove(os.path.join(app.config['UPLOAD_PATH'],  file.filename))
            print("process completed")
            return render_template('output.html',summary = output["summary"], positives =  output["positives"], negatives = output["negatives"],tech = output["tech-jargon"] ) 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)