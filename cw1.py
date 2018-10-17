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
#year
@app.route("/movies/1994/")
def y1994():
    year=1994
    movies=['The Shawshank Redemption','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    moviesLink=['theshawshankredemtion/','theshawshankredemtion/']
    mylist = zip(movies, moviesLink)
    return render_template('year.html', year=year, mylist=mylist)

#genres
@app.route("/movies/drama/")
def drama():
    genre='Drama'
    history = ['Drama is a genre of narrative fiction(or semi-fiction) intended to be more serious than humorous in tone. Drama of this kind is usually qualified with additional terms that specify its particular subgenre, such as \'police creme drama\', \'political drama\', \'legal drama\', \'historical period drama\', \'domestic drama\', or \'comedy drama\'. Theses terms tend to indicate a particular setting of subject-matter, or else they qualify the otherwise serious tone of a drama with elements that encourage a broader range of moods.','All forms of cinema or television that involve fictional stories are forms of drama in the broader sense if their storytelling is achieved by means of actors who represent characters. In this broader sense, drama is a mode distinct from novels, short stories, and narrrative poetry or songs. In the modern era before the birth of cinema or television, \'drama\' came to be used within the theatre as a generic term to describe a type of play that was neither a comedy nor a tragedy.It is this narrower sense that the film and television industries, along with film studies, adopted. \'Radio drama\' has been used in both senses—originally transmitted in a live performance, it has also been used to describe the more high-brow and serious end of the dramatic output of radio.']
    movies=['The Shawshank Redemption','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    moviesLink=['theshawshankredemtion/','theshawshankredemtion/']
    mylist = zip(movies, moviesLink)
    return render_template('genres.html', genre=genre, history=history, mylist=mylist)

@app.route("/movies/adventure/")
def adventure():
    genre='Adventure'
    history = [' Adventure Films are exciting stories, with new experiences or exotic locales. Adventure films are very similar to the action film genre, in that they are designed to provide an action-filled, energetic experience for the film viewer. Rather than the predominant emphasis on violence and fighting that is found in action films, however, the viewer of adventure films can live vicariously through the travels, conquests, explorations, creation of empires, struggles and situations that confront the main characters, actual historical figures or protagonists.','Adventure films were intended to appeal mainly to men, creating major male heroic stars through the years. These courageous, patriotic, or altruistic heroes often fought for their beliefs, struggled for freedom, or overcame injustice. Modern adventure films, some of which have been successful blockbusters, have crossed over and added resourceful action heroes (and oftentimes heroines).','Under the category of adventure films, we can include traditional swashbucklers, serialized films, and historical spectacles (similar to the epics film genre), searches or expeditions for lost continents, "jungle" and "desert" epics, treasure hunts and quests, disaster films, and heroic journeys or searches for the unknown. Adventure films are often set in an historical period, and may include adapted stories of historical or literary adventure heroes (Robin Hood, Tarzan, and Zorro for example), kings, battles, rebellion, or piracy.']
    movies=['The Shawshank Redemption','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    moviesLink=['theshawshankredemtion/','theshawshankredemtion/']
    mylist = zip(movies, moviesLink)
    return render_template('genres.html', genre=genre, history=history, mylist=mylist)

@app.route("/movies/comedy/")
def comedy():
    genre='Comedy'
    history = ['Comedy Films are "make \'em laugh" films designed to elicit laughter from the audience. Comedies are light-hearted dramas, crafted to amuse, entertain, and provoke enjoyment. The comedy genre humorously exaggerates the situation, the language, action, and characters. Comedies observe the deficiencies, foibles, and frustrations of life, providing merriment and a momentary escape from day-to-day life. They usually have happy endings, although the humor may have a serious or pessimistic side.','Comedies usually come in two general formats: comedian-led (with well-timed gags, jokes, or sketches) and situation-comedies that are told within a narrative. Both comedy elements may appear together and/or overlap. Comedy hybrids commonly exist with other major genres, such as musical-comedy, horror-comedy, and comedy-thriller. Comedies have also been classified in various subgenres, such as romantic comedy, crime/caper comedy, sports comedy, teen or coming-of-age comedy, social-class comedy, military comedy, fish-out-of-water comedy, and gross-out comedy.']
    movies=['The Shawshank Redemption','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    moviesLink=['theshawshankredemtion/','theshawshankredemtion/']
    mylist = zip(movies, moviesLink)
    return render_template('genres.html', genre=genre, history=history, mylist=mylist)

@app.route("/movies/crime/")
def crime():
    genre='Crime'
    history = ['Crime and Gangster Films are developed around the sinister actions of criminals or gangsters, particularly bankrobbers, underworld figures, or ruthless hoodlums who operate outside the law, stealing and violently murdering their way through life. In the 1940s, a new type of crime thriller emerged, more dark and cynical - see the section on film-noir for further examples of crime films. Criminal and gangster films are often categorized as post-war film noir or detective-mystery films - because of underlying similarities between these cinematic forms. Crime films encompass or cross over many levels, and may include at least these different types of films: the gangster film, the detective (or who-dun-it) film, the crime comedy, the suspense-thriller, and the police (procedural) film.','Crime stories in this genre often highlight the life of a crime figure or a crime\'s victim(s). Or they glorify the rise and fall of a particular criminal(s), gang, bank robber, murderer or lawbreakers in personal power struggles or conflict with law and order figures, an underling or competitive colleague, or a rival gang. Headline-grabbing situations, real-life gangsters, or crime reports have often been used in crime films. Gangster/crime films are usually set in large, crowded cities, to provide a view of the secret world of the criminal: dark nightclubs or streets with lurid neon signs, fast cars, piles of cash, sleazy bars, contraband, seedy living quarters or rooming houses. Exotic locales for crimes often add an element of adventure and wealth. Writers dreamed up appropriate gangland jargon for the tales, such as "tommy guns" or "molls."','Film gangsters are usually materialistic, street-smart, immoral, meglo-maniacal, and self-destructive. Rivalry with other criminals in gangster warfare is often a significant plot characteristic. Crime plots also include questions such as how the criminal will be apprehended by police, private eyes, special agents or lawful authorities, or mysteries such as who stole the valued object. They rise to power with a tough cruel facade while showing an ambitious desire for success and recognition, but underneath they can express sensitivity and gentleness.']
    movies=['The Shawshank Redemption','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    moviesLink=['theshawshankredemtion/','theshawshankredemtion/']
    mylist = zip(movies, moviesLink)
    return render_template('genres.html', genre=genre, history=history, mylist=mylist)

@app.route("/movies/historical/")
def historical():
    genre='Historical'
    history = ['Epics-Historical Films often take an historical or imagined event, mythic, legendary, or heroic figure, and add an extravagant setting and lavish costumes, accompanied by grandeur and spectacle and a sweeping musical score. Epics, costume dramas, historical dramas, war film epics, medieval romps, or \'period pictures\' are tales that often cover a large expanse of time set against a vast, panoramic backdrop. In an episodic manner, they follow the continuing adventures of the hero(s), who are presented in the context of great historical events of the past.','Epics are historical films that recreate past events. They are expensive and lavish to produce, because they require elaborate and panoramic settings, on-location filming, authentic period costumes, inflated action on a massive scale and large casts of characters. Biopic (biographical) films are often less lavish versions of the epic film.','Epics often rewrite history, suffering from inauthenticity, fictitious recreations, excessive religiosity, hard-to-follow details and characters, romantic dreamworlds, ostentatious vulgarity, political correctness, and leaden scripts.']
    movies=['The Shawshank Redemption','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    moviesLink=['theshawshankredemtion/','theshawshankredemtion/']
    mylist = zip(movies, moviesLink)
    return render_template('genres.html', genre=genre, history=history, mylist=mylist)

@app.route("/movies/horror/")
def horror():
    genre='Horror'
    history = ['Horror Films are unsettling films designed to frighten and panic, cause dread and alarm, and to invoke our hidden worst fears, often in a terrifying, shocking finale, while captivating and entertaining us at the same time in a cathartic experience. Horror films effectively center on the dark side of life, the forbidden, and strange and alarming events. They deal with our most primal nature and its fears: our nightmares, our vulnerability, our alienation, our revulsions, our terror of the unknown, our fear of death and dismemberment, loss of identity, or fear of sexuality.','Whatever dark, primitive, and revolting traits that simultaneously attract and repel us are featured in the horror genre. Horror films are often combined with science fiction when the menace or monster is related to a corruption of technology, or when Earth is threatened by aliens. The fantasy and supernatural film genres are not synonymous with the horror genre, although thriller films may have some relation when they focus on the revolting and horrible acts of the killer/madman. Horror films are also known as chillers, scary movies, spookfests, and the macabre. See also Scariest Film Moments and Scenes (illustrated) - from many of the Greatest Horror Films ever made, Best Film Death Scenes (illustrated), and Three Great Horror Film Franchises.']
    movies=['The Shawshank Redemption','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    moviesLink=['theshawshankredemtion/','theshawshankredemtion/']
    mylist = zip(movies, moviesLink)
    return render_template('genres.html', genre=genre, history=history, mylist=mylist)

@app.route("/movies/sciencefiction/")
def sciencefiction():
    genre='Science Fiction'
    history = ['Science Fiction Films are usually scientific, visionary, comic-strip-like, and imaginative, and usually visualized through fanciful, imaginative settings, expert film production design, advanced technology gadgets (i.e., robots and spaceships), scientific developments, or by fantastic special effects. Sci-fi films are complete with heroes, distant planets, impossible quests, improbable settings, fantastic places, great dark and shadowy villains, futuristic technology and gizmos, and unknown and inexplicable forces. Many other SF films feature time travels or fantastic journeys, and are set either on Earth, into outer space, or (most often) into the future time. Quite a few examples of science-fiction cinema owe their origins to writers Jules Verne and H.G. Wells.','They often portray the dangerous and sinister nature of knowledge (\'there are some things Man is not meant to know\') (i.e., the classic Frankenstein (1931), The Island of Lost Souls (1933), and David Cronenberg\'s The Fly (1986) - an updating of the 1958 version directed by Kurt Neumann and starring Vincent Price), and vital issues about the nature of mankind and our place in the whole scheme of things, including the threatening, existential loss of personal individuality (i.e., Invasion of the Body Snatchers (1956), and The Incredible Shrinking Man (1957)). Plots of space-related conspiracies (Capricorn One (1977)), supercomputers threatening impregnation (Demon Seed (1977)), the results of germ-warfare (The Omega Man (1971)) and laboratory-bred viruses or plagues (28 Days Later (2002)), black-hole exploration (Event Horizon (1997)), and futuristic genetic engineering and cloning (Gattaca (1997) and Michael Bay\'s The Island (2005)) show the tremendous range that science-fiction can delve into.']
    movies=['The Shawshank Redemption','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    moviesLink=['theshawshankredemtion/','theshawshankredemtion/']
    mylist = zip(movies, moviesLink)
    return render_template('genres.html', genre=genre, history=history, mylist=mylist)

@app.route("/movies/war/")
def war():
    genre='War'
    history = ['War and Anti-War Films often acknowledge the horror and heartbreak of war, letting the actual combat fighting or conflict (against nations or humankind) provide the primary plot or background for the action of the film. Typical elements in the action-oriented war plots include POW camp experiences and escapes, submarine warfare, espionage, personal heroism, "war is hell" brutalities, air dogfights, tough trench/infantry experiences, or male-bonding buddy adventures during wartime. Themes explored in war films include combat, survivor and escape stories, tales of gallant sacrifice and struggle, studies of the futility and inhumanity of battle, the effects of war on society, and intelligent and profound explorations of the moral and human issues.','Some war films do balance the soul-searching, tragic consequences and inner turmoil of combatants or characters with action-packed, dramatic spectacles, enthusiastically illustrating the excitement and turmoil of warfare. And some \'war\' films concentrate on the homefront rather than on the conflict at the military war-front. But many of them provide decisive criticism of senseless warfare.','War films have often been used as \'flag-waving\' propaganda to inspire national pride and morale, and to display the nobility of one\'s own forces while harshly displaying and criticizing the villainy of the enemy, especially during war or in post-war periods. Jingoistic-type war films usually do not represent war realistically in their support of nationalistic interests, while avoiding the reality of the horrors of war. The good guys are portrayed as clashing against the bad guys (often with stereotyped labels such as \'krauts,\' \'commies,\' \'Huns,\' or \'nips\'). These revisionistic, politically-correct and historically inaccurate films, in such diverse examples as Sands of Iwo Jima (1949) and The Alamo (1960), would often redefine the facts.']
    movies=['The Shawshank Redemption','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    moviesLink=['theshawshankredemtion/','theshawshankredemtion/']
    mylist = zip(movies, moviesLink)
    return render_template('genres.html', genre=genre, history=history, mylist=mylist)

@app.route("/movies/western/")
def western():
    genre='Western'
    history = ['Westerns are the major defining genre of the American film industry, a nostalgic eulogy to the early days of the expansive, untamed American frontier (the borderline between civilization and the wilderness). They are one of the oldest, most enduring and flexible genres and one of the most characteristically American genres in their mythic origins.','This indigenous American art form focuses on the frontier West that existed in North America. Westerns are often set on the American frontier during the last part of the 19th century (1865-1900) following the Civil War, in a geographically western (trans-Mississippi) setting with romantic, sweeping frontier landscapes or rugged rural terrain. However, Westerns may extend back to the time of America\'s colonial period or forward to the mid-20th century, or as far geographically as Mexico. A number of westerns use the Civil War, the Battle of the Alamo (1836) or the Mexican Revolution (1910) as a backdrop.']
    movies=['The Shawshank Redemption','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    moviesLink=['theshawshankredemtion/','theshawshankredemtion/']
    mylist = zip(movies, moviesLink)
    return render_template('genres.html', genre=genre, history=history, mylist=mylist)

@app.route("/movies/1994/theshawshankredemtion/")
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
    plot=["In 1947 Portland, Maine, banker Andy Dufresne is convicted of murdering his wife and her lover, and sentenced to two consecutive life sentences at the Shawshank State Penitentiary. He is befriended by Ellis Red Redding, an inmate and prison contraband smuggler serving a life sentence. Red procures a rock hammer and a large poster of Rita Hayworth for Andy. Working in the prison laundry, Andy is regularly assaulted and raped by the Sisters and their leader, Bogs.",
    "In 1949, Andy overhears the captain of the guards, Byron Hadley, complaining about being taxed on an inheritance and offers to help him shelter the money legally. After an assault by the Sisters nearly kills Andy, Hadley beats and cripples Bogs, who is subsequently transferred to another prison; Andy is not attacked again. Warden Samuel Norton meets Andy and reassigns him to the prison library to assist elderly inmate Brooks Hatlen. Andy begins managing financial matters for other prison staff, guards from other prison, and the warden himself. He also begins writing weekly letters to the state legislature requesting funds to improve the prisons decaying library.",
    "Brooks is paroled in 1954 after serving 50 years, but he cannot adjust to the outside world and eventually hangs himself. The legislature sends a library donation that includes a recording of The Marriage of Figaro. Andy plays an excerpt over the public address system and is punished with solitary confinement. After his release from solitary, Andy explains that hope is what gets him through his time, a concept that Red dismisses. In 1963, Norton begins exploiting prison labor for public works, profiting by undercutting skilled labor costs and receiving bribes. Andy launders the money using the alias Randall Stephens."]
    time='114 minutes'
    casting=['Tim Robbins','Morgan Freeman','Bob Gunton','William Sadler','Clancy Brown','Gil Bellows','James Whitmore']
    budget='$25 millions'
    boxoffice='$53.8 millions'
    return render_template('movieInfo.html',movie=movie,poster=poster,director=director,producer=producer,genre=genre,genreLink=genreLink,year=year,plot=plot,time=time,casting=casting,budget=budget,boxoffice=boxoffice)

#Working with Errorst
@app.route('/force404')
def force404():
	abort(404)

@app.errorhandler(404)
def page_not_found(error):
    message ="Couldn't find the page you requested"
    return render_template('message.html', message=message), 404

#redirect


if __name__==" __main__ ":
    app.run(host ='0.0.0.0',debug=True)
