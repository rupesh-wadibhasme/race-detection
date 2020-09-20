import os,json,shutil
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from rest_api import *
app = Flask(__name__)
cwd = os.getcwd()
UPLOAD_FOLDER = os.path.join(cwd,"uploads")
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])

IMAGE_EXTENSIONS=set(['png','jpg','jpeg'])


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            #flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            if filename.rsplit('.', 1)[1].lower() in IMAGE_EXTENSIONS:
                output = race_det(os.path.join(UPLOAD_FOLDER,filename))
            output=json.dumps(output)
        os.remove(os.path.join(UPLOAD_FOLDER,filename))
        return output
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
    #return

if __name__ == '__main__':
   app.run("0.0.0.0",port=8005,threaded=True,debug=False)
