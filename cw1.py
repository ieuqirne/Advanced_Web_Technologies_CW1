from flask import Flask, render_template, request, url_for, redirect, flash
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

#genres
@app.route("/movies/drama/")
def drama():
    genre='Drama'
    history= "Drama is a genre of narrative fiction(or semi-fiction) intended to be more serious than humorous in tone. Drama of this kind is usually qualified with additional terms that specify its particular subgenre, such as 'police creme drama', 'political drama', 'legal drama', 'historical period drama', 'domestic drama, or 'comedy drama'. Theses terms tend to indicate a particular setting of subject-matter, or else they qualify the otherwise serious tone of a drama with elements that encourage a broader range of moods."
    history1= "All forms of cinema or television that involve fictional stories are forms of drama in the broader sense if their storytelling is achieved by means of actors who represent characters. In this broader sense, drama is a mode distinct from novels, short stories, and narrrative poetry or songs. In the modern era before the birth of cinema or television, 'drama' came to be used within the theatre as a generic term to describe a type of play that was neither a comedy nor a tragedy. It is this narrower sense that the film and television industries, along with film studies, adopted. 'Radio drama' has been used in both senses—originally transmitted in a live performance, it has also been used to describe the more high-brow and serious end of the dramatic output of radio."
    movies=['The Shawshank Redemption','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    moviesLink=['theshawshankredemtion/','theshawshankredemtion/']
    mylist = zip(movies, moviesLink)
    return render_template('genres.html', genre=genre, history=history, history1=history1, mylist=mylist)

@app.route("/movies/drama/theshawshankredemtion/")
@app.route("/movies/theshawshankredemtion/")
def theshawshankredemtion():
    movie='The Shawshank Redemption'
    poster= url_for('static', filename='posters/0000000001.jpg')
    director='Frank Darabont'
    producer='Niki Marvin'
    genre='Drama'
    genreLink='drama'
    year='1994'
    plot=['In 1947 Portland, Maine, banker Andy Dufresne is convicted of murdering his wife and her lover, and sentenced to two consecutive life sentences at the Shawshank State Penitentiary. He is befriended by Ellis Red Redding, an inmate and prison contraband smuggler serving a life sentence. Red procures a rock hammer and a large poster of Rita Hayworth for Andy. Working in the prison laundry, Andy is regularly assaulted and raped by the Sisters and their leader, Bogs.',
    'In 1949, Andy overhears the captain of the guards, Byron Hadley, complaining about being taxed on an inheritance and offers to help him shelter the money legally. After an assault by the Sisters nearly kills Andy, Hadley beats and cripples Bogs, who is subsequently transferred to another prison; Andy is not attacked again. Warden Samuel Norton meets Andy and reassigns him to the prison library to assist elderly inmate Brooks Hatlen. Andy begins managing financial matters for other prison staff, guards from other prison, and the warden himself. He also begins writing weekly letters to the state legislature requesting funds to improve the prisons decaying library.',
    'Brooks is paroled in 1954 after serving 50 years, but he cannot adjust to the outside world and eventually hangs himself. The legislature sends a library donation that includes a recording of The Marriage of Figaro. Andy plays an excerpt over the public address system and is punished with solitary confinement. After his release from solitary, Andy explains that hope is what gets him through his time, a concept that Red dismisses. In 1963, Norton begins exploiting prison labor for public works, profiting by undercutting skilled labor costs and receiving bribes. Andy launders the money using the alias Randall Stephens.']
    time='114 minutes'
    casting=['Tim Robbins','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    budget='$25 millions'
    boxoffice='$53.8 millions'
    return render_template('tableshow.html',movie=movie,poster=poster,director=director,producer=producer,genre=genre,genreLink=genreLink,year=year,plot=plot,time=time,casting=casting,budget=budget,boxoffice=boxoffice)

#redirect


if __name__==" __main__ ":
    app.run(host ='0.0.0.0',debug=True)
