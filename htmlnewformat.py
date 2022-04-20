import re
import json
import csv
import os
import pandas as pd
import numpy as np
from IPython.display import display
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

                            temp = soup.title
                           
                           #Filtering the username from the file
                           #The username of the profile
                            username = str(temp)
                           #split the first half of the string we don't want
                            username = username.split(">", 1)[1]
                           #split the second half
                            username = username.split("<", 1)[0]

                            #redo rating here later for now allow it to be 'na'
                            rating = 'na'
                            
                            temp = soup.find_all("pre")
                           
                            print(len(temp)) 
                           
                            #If it has both description and PGP
                            if len(temp) == 2:
                           # user provided description
                                description = str(temp[0])
                               
                               #find the email addresses listed within the description (user email)
                                if re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', description) == []:
                                    emails = 'na'
                                else:
                                    emails = str(re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', description))
                               
                               #PGP key utilized
                                PGP = str(temp[1])
                               #split first half of PGP
                                PGP = PGP.split(">", 1)[1]
                               #split second half of PGP
                                PGP = PGP.split("<", 1)[0]
                                
                            #If it only have 1 of description and PGP (determining which)
                            elif len(temp) == 1:
                           
                                if re.findall("PGP", str(temp[0])) == []:
                                    
                                    if re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', str(temp[0])) == []:
                                        emails = 'na'
                                    else:
                                        emails = str(re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', description))
                                        
                                    PGP = 'na'
                                else:
                                   #PGP key utilized
                                    PGP = str(temp[1])
                                   #split first half of PGP
                                    PGP = PGP.split(">", 1)[1]
                                   #split second half of PGP
                                    PGP = PGP.split("<", 1)[0]
                                    
                                    emails = 'na'
                            #If the file contains neither description or PGP
                            else:
                                PGP = 'na'
                                emails = 'na'
                            
                            
                            
                            df2 = pd.DataFrame({'Username': username, 'Rating': rating, 'Email': emails, 'PGP': PGP}, index=[0])
                           
                            df = df.append(df2)
                           
                            
                            print(count)
#display(df)
df.to_csv('HydraNewFormatUsers.csv')