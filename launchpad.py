__author__ = 'Nikhil'
import os
import requests
import csv

movie_list = []
yearlisttmp = list(range(1990, 2050))
yearlist = [str(x) for x in yearlisttmp]

input("If you are Online I can get you the ratings of movies in this folder, may I ?")
for root, dirs, files in os.walk("."):
    for names in files:
        if ((names.find('.mp4') != -1) or (names.find('.avi') != -1) or (names.find('.mkv') !=-1)) :
            for year in yearlist:
                if names.find(year) != -1:
                    trimmed_title = names[:names.find(year)+4]
                    if trimmed_title.find('.') != -1:
                        trimmed_title = trimmed_title.replace('.', ' ')
                    if trimmed_title.find('(') != -1:
                        trimmed_title = trimmed_title.replace('(', '')
                    if trimmed_title.find(')') != -1:
                        trimmed_title = trimmed_title.replace(')', '')
                    if trimmed_title.find('[') != -1:
                        trimmed_title = trimmed_title.replace('[', '')
                    if trimmed_title.find(']') != -1:
                        trimmed_title = trimmed_title.replace(']', '')
                    if trimmed_title.find('  ') != -1:
                        trimmed_title = trimmed_title.replace('  ', ' ')
                    print(trimmed_title)
                    trimmed_title = trimmed_title.strip()

            movie_list.append(trimmed_title)
# print(movie_list)


for movies in movie_list:
    for year in yearlist:
        if movies.find(year) != -1:
            title = movies[:movies.find(year)]
            # title = title.replace(' ', '+')
            payload = {'t': title, 'y': year, 'r': 'jason', 'tomatoes': 'true'}
            response = requests.get('http://www.omdbapi.com/', params=payload)
            print(response.status_code)
            if (response.status_code == 200):
                jsonres = response.json()
                imdbRating = str(jsonres.get("imdbRating"))
                imdbVotes = str(jsonres.get("imdbVotes"))
                tomatoMeter = str(jsonres.get("tomatoMeter"))
                tomatoUserMeter = str(jsonres.get("tomatoUserMeter"))
                print("-----------------------------------------------")
                print("Title:" + title)
                print("IMDB Rating:"+ imdbRating)
                print("IMDB Votes:"+ imdbVotes)
                print("Tomato Meter:"+ tomatoMeter)
                print("Tomato User Meter:"+ tomatoUserMeter)
                #print(jsonres.url)
                print("-----------------------------------------------") 
                with open('eggs.csv', 'a') as csvfile:
                    try:
                        spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
                        spamwriter.writerow([title , imdbRating, imdbVotes, tomatoMeter, tomatoUserMeter])
                    except csv.Error as e:
                        sys.exit('Error %s' % (e))
input("Thank you, Happy Watching Movie...")
