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
df = pd.DataFrame({'Username': ['temp'], 'Account Type': ['temp'], 'Rating': ['temp'], 'Email': ['temp'], 'PGP': ['temp']})

print ("All files ending with .html in folder %s:" % rootdir)
file_list = []
#for paths, dirs, files in scandir.walk(rootdir):

for (paths, dirs, files) in os.walk(rootdir):
            for file in files:
#used for test casing if an email did not exist               
#with open("/mnt/d/Desktop/Darkweb Research Data/hydra/hydra-old-format/2014-05-22/vendor/TrueBlue.html") as fp:
#with open("/mnt/d/Desktop/Darkweb Research Data/pandora/2013-12-25/profile/0083d8cce6ec8db4b56b6af34bd792c5") as fp:
                if file == "htmlpandoraformat.py" or file == "pandoracleanup.py" or file == "PandoraUsers.csv":
                    continue
                else:
                    with open(os.path.join(paths, file)) as fp:
                        print(str(os.path.join(paths, file)))
                                
                                
                        count += 1
                            
                        soup = BeautifulSoup(fp)

                        temp = soup.find_all("h2")
                           
                        print(temp)
                        
                        if temp == []:
                            username = 'na'
                        else:
                        
                           #Filtering the username from the file
                           #The username of the profile
                            username = str(temp[0])
                           #split the first half of the string we don't want
                            username = username.split(" ", 2)[2]
                           #split the second half
                            username = username.split("<", 1)[0]
                      
                        #print(username)
                        
                        temp = soup.find_all("td")
                        
                        """ Find the indexs for rating and account type
                        count2 =0
                        
                        for i in temp:
                            print(i)
                            count2 += 1
                            print(count2)
                            
                        print(temp[6])
                        print(temp[9])
                        """
                        if temp == []:
                            accountType = 'na'
                        else:
                           #accountType
                            accountType = str(temp[6])
                           #split first half of accountType
                            accountType = accountType.split(">", 2)[2]
                           #split second half of accountType
                            accountType = accountType.split(":", 1)[0]
                        
                        #print(accountType)
                        
                        if temp == []:
                            rating = 'na'
                        else:
                           #rating out of 5
                            rating = str(temp[9])
                           #split first half of rating
                            rating = rating.split(">", 1)[1]
                           #split second half of rating
                            rating = rating.split("<", 1)[0]
                        
                        #print(rating)

                        temp = soup.find_all("pre")
                   
                        if temp == []:
                       # user provided description
                            emails = 'na'
                        else:
                            description = str(temp[0])
                           
                           #find the email addresses listed within the description (user email)
                            if re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', description) == []:
                                emails = 'na'
                            else:
                                emails = str(re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', description))
                           
                        #print(emails)
                        
                        temp = soup.find_all("textarea")
                        
                        if temp == []:
                       #PGP key utilized
                            PGP = 'na'
                        else:
                            PGP = str(temp[0])
                           
                           #split first half of PGP
                            PGP = PGP.split(">", 1)[1]
                           #split second half of PGP
                            PGP = PGP.split("<", 1)[0]
                            
                        #print(PGP)
                        
                        df2 = pd.DataFrame({'Username': username, 'Account Type': accountType, 'Rating': rating, 'Email': emails, 'PGP': PGP}, index=[0])
                        
                        df = df.append(df2)
                       
                        #display(df2)
                       
                        
                        print(count)

#display(df)
df.to_csv('PandoraUsers.csv')