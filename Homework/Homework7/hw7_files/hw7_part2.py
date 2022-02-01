import json
'''Checks the for the best rated movie'''
def best():
    max = 0
    maxname = ''
    maxyearm = 0
    yeslist = []
    maxmovie = dict()
    #goes through the movies and sees if it is between the years and in the genre
    for i in movies:
        if (genre in movies[i]['genre']) and ((movies[i]['movie_year'] >= minyear) and movies[i]['movie_year'] <= maxyear) :
            yeslist.append(i)
    for i in yeslist:
        imdb_rating = movies[i]['rating']
        try: #sees if there is a twitter rating, if not skips
            average_twitter_rating = sum(ratings[i])/len(ratings[i])
        except KeyError:
            continue
        if len(ratings[i]) < 3:
            continue
        #does the calculating
        score = ((imdb * imdb_rating) + (twitter * average_twitter_rating)) / (imdb + twitter)
        if score >= max: #if the score is higher than the max then replace the max movie
            max = score
            maxname = movies[i]['name']
            maxyearm = movies[i]['movie_year']
    #if there is a movie found print
    if max != 0:
        print('Best:')
        print('        Released in {}, {} has a rating of {:.02f}'.format(maxyearm, maxname, max))
        print()
        worst()
    else:
        none()
'''Same function just checks for the lowest rating'''
def worst():
    min = 10000
    minname = ''
    minyearm = 0
    yeslist = []
    for i in movies:
        if (genre in movies[i]['genre']) and ((movies[i]['movie_year'] >= minyear) and movies[i]['movie_year'] <= maxyear) :
            yeslist.append(i)
    for i in yeslist:
        imdb_rating = movies[i]['rating']
        try:
            average_twitter_rating = sum(ratings[i])/len(ratings[i])
        except KeyError:
            continue
        if len(ratings[i]) < 3:
            continue
        score = ((imdb * imdb_rating) + (twitter * average_twitter_rating)) / (imdb + twitter)
        if score < min:
            min = score
            minname = movies[i]['name']
            minyearm = movies[i]['movie_year']

    if min != 10000:
        print('Worst:')
        print('        Released in {}, {} has a rating of {:.02f}'.format(minyearm, minname, min))
        print()
    else:
        pass

'''If there are no movies found then it calls and prints this function'''
def none():
    print('No {} movie found in {} through {}'.format(genre, minyear, maxyear))
    print()

if __name__ == "__main__":
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())

    minyear = int(input('Min year => '))
    print(minyear)
    maxyear = int(input('Max year => '))
    print(maxyear)
    imdb = input('Weight for IMDB => ')
    print(imdb)
    imdb = float(imdb)
    twitter = input('Weight for Twitter => ')
    print(twitter)
    twitter = float(twitter)
    print()
    glist = []
    for i in movies:
        glist.append(movies[i]['genre'])
    #flattens the list of genres
    flat_list = [item for sublist in glist for item in sublist]
    flat_list = set(flat_list)
    genre = ''
    #forever loop
    while True:
        genre = input('What genre do you want to see? ')
        print(genre)
        genre = genre.title()
        if genre in flat_list:
            print()
            best()
        elif genre == 'Stop':
            exit()
        else:
            print()
            none()