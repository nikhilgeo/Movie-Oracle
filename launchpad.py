__author__ = 'Nikhil'
import os
import requests

movie_list = []
yearlisttmp = list(range(1990, 2050))
yearlist = [str(x) for x in yearlisttmp]

input("If you are Online I can get you the ratings of movies in this folder, may I ?")

for root, dirs, files in os.walk("."):
    for names in files:
        if ((names.find('.mp4') != -1) or (names.find('.avi') != -1) or (names.find('.mvk') !=-1)) :
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
                print("-----------------------------------------------")
                print("Title:" + title)
                print("IMDB Rating:"+str(jsonres.get("imdbRating")))
                print("IMDB Votes:"+str(jsonres.get("imdbVotes")))
                print("Tomato Meter:"+str(jsonres.get("tomatoMeter")))
                print("Tomato User Meter:"+str(jsonres.get("tomatoUserMeter")))
                #print(jsonres.url)
                print("-----------------------------------------------") 
input("Thank you, Happy Watching Movie...")
