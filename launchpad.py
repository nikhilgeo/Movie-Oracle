__author__ = 'Nikhil'
import os
import requests
import csv
import re

movie_list = []
yearlisttmp = list(range(1990, 2050))
yearlist = [str(x) for x in yearlisttmp]
regexYear = re.compile('\d{4}')

# Function to get the rating from omdbapi : Start
def getRatings(title,year):
    payload = {'t': title, 'y': year, 'r': 'jason', 'tomatoes': 'true'}
    response = requests.get('http://www.omdbapi.com/', params=payload)
    print("-----------------------------------------------")
    print("Title:" + title)
    print("Response Code:" + str(response.status_code))
    if (response.status_code == 200):
        jsonres = response.json()
        imdbRating = str(jsonres.get("imdbRating"))
        imdbVotes = str(jsonres.get("imdbVotes"))
        tomatoMeter = str(jsonres.get("tomatoMeter"))
        tomatoUserMeter = str(jsonres.get("tomatoUserMeter"))
        print("IMDB Rating:"+ imdbRating)
        print("IMDB Votes:"+ imdbVotes)
        print("Tomato Meter:"+ tomatoMeter)
        print("Tomato User Meter:"+ tomatoUserMeter)
        #print(jsonres.url)
        with open('MovieRatings.csv', 'a') as csvfile:
            try:
                csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
                csvwriter.writerow([title , imdbRating, imdbVotes, tomatoMeter, tomatoUserMeter])
            except csv.Error as e:
                sys.exit('Error %s' % (e))
    print("-----------------------------------------------") 
    return
# Function to get the rating from omdbapi : End



print("Fetching all the movie rating, will try my BEST !!")

# Put the coloumn Header in the CSV files in advance
with open('MovieRatings.csv', 'a') as csvfile:
            try:
                csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
                csvwriter.writerow(["title" , "imdbRating", "imdbVotes", "tomatoMeter", "tomatoUserMeter"])
            except csv.Error as e:
                sys.exit('Error %s' % (e))

for root, dirs, files in os.walk("."):
    for names in files:
        year = ""
        trimmed_title = ""
        if (names.lower().endswith(('.mp4', '.mkv', '.avi'))):
            trimmed_title = names[:-4]

            # Search for Year
            regexresult = regexYear.search(names)
            if regexresult is not None:
                year = regexresult.group()
                yearStartIndex = regexresult.start()
                trimmed_title = names[:yearStartIndex]

            # Title sanitation
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
            if trimmed_title.find('{') != -1:
                trimmed_title = trimmed_title.replace('{', '')
            if trimmed_title.find('}') != -1:
                trimmed_title = trimmed_title.replace('}', '')
            if trimmed_title.find('  ') != -1:
                trimmed_title = trimmed_title.replace('  ', ' ')
            trimmed_title = trimmed_title.strip()      
            # print(trimmed_title)
            # print(year)
            getRatings(trimmed_title,year)
input("Thank you, Happy Watching Movie...")

