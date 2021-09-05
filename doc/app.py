from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import time
import optimizer



app = Flask(__name__)

root = os.path.join(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = root + '/temp/'

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/upload')
def up():
    return render_template("uploader.html")

@app.route('/image-optimize', methods = ['POST'])
def img_optimizer():
    if 'image' in request.files:
        f = request.files['image']
        file_name = str(time.time() * 1000) + secure_filename(f.filename)
        file_path = UPLOAD_FOLDER + file_name
        try:
            f.save(file_path)
        except:
            return {"status": "error", "message":"file write error"}
        
        res = optimizer.optimize(file_name)
        if res["status"] == "success":
            res["filename"] = secure_filename(f.filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        return res
    else:
        return {"status": "error", "message": "file required"}
    

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000)

    # app.run( port=5000)
