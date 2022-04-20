import re
import json
import csv
import os
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import scandir

rootdir = os.getcwd()

count = 0
df = pd.DataFrame({'Username': ['temp'], 'Rating': ['temp'], 'Email': ['temp'], 'PGP': ['temp']})

print ("All files ending with .html in folder %s:" % rootdir)
file_list = []

#for paths, dirs, files in scandir.walk(rootdir):
for (paths, dirs, files) in os.walk(rootdir):
            for file in files:
                if file.endswith(".html"):
                    if file != "index.html":
                        with open(os.path.join(paths, file)) as fp:
                            print(str(os.path.join(paths, file)))
                            
                            
                            count += 1
                            
                            soup = BeautifulSoup(fp)

                            temp = soup.find_all("h2")
                           
                           #Filtering the username from the file
                           #The username of the profile
                            username = str(temp[0])
                           #split the first half of the string we don't want
                            username = username.split(">", 3)[3]
                           #split the second half
                            username = username.split("<", 3)[0]
                           #remove the whitespace in the first character of every entry
                            username = username.split(" ", 1)[1]
                           
                           #rating out of 5
                            rating = str(temp[1])
                           #split first half of rating
                            rating = rating.split(">", 1)[1]
                           #split second half of rating
                            rating = rating.split("<", 1)[0]
                           
                            temp = soup.find_all("pre")
                           
                           # user provided description
                            description = str(temp[0])
                           
                           #find the email addresses listed within the description (user email)
                            emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', description)
                           
                           #PGP key utilized
                            PGP = str(temp[1])
                           
                           #split first half of PGP
                            PGP = PGP.split(">", 1)[1]
                           #split second half of PGP
                            PGP = PGP.split("<", 1)[0]
                           
                            df2 = pd.DataFrame({'Username': username, 'Rating': rating, 'Email': emails, 'PGP': PGP})
                           
                            df = df.append(df2)
                           
                            
                            print(count)
#display(df)