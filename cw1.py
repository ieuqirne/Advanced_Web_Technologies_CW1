from flask import Flask , render_template, request
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('base.html'),200

#uploading data
@app.route("/uploading/", methods=['POST','GET'])
def uploading():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/img/file.png')
        return "File Uploaded"
    else:
        return render_template('uploading.html')



if __name__==" __main__ ":
    app.run(host ='0.0.0.0',debug=True)
