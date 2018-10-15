from flask import Flask , render_template, request, url_for,redirect, flash
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

@app.route("/genre/drama/theshawshankredemtion/")
@app.route("/movies/theshawshankredemtion/")
def theshawshankredemtion():
    movie='The Shawshank Redemption'
    poster= url_for('static', filename='posters/0000000001.jpg')
    director='Frank Darabont'
    producer='Niki Marvin'
    genre='Drama'
    year='1994'
    plot=''
    time='48:49'
    casting=['Tim Robbins','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    budget='$25 millions'
    boxoffice='$53.8 millions'
    return render_template('tableshow.html',movie=movie,poster=poster,director=director,producer=producer,genre=genre,year=year,plot=plot,time=time,casting=casting,budget=budget,boxoffice=boxoffice)



if __name__==" __main__ ":
    app.run(host ='0.0.0.0',debug=True)
