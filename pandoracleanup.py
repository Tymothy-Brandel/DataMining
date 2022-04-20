import os

rootdir = os.getcwd()

#this script removes all other directories that was not "vender" from the
#different dates that Hydra was scraped.This is done because for the time
#being we are only looking at vendor data.

#removed pandora/2014-06-09
#removed pandora/2014-07-28
#removed pandora/2014-10-16
#removed pandora/2014-10-27
"""
for subdir, dirs, files in os.walk(rootdir):
    for subdir in dirs:
"""

file_list = ["2013-12-25", "2014-04-20", "2014-06-24", "2014-08-18", "2014-09-12", "2014-10-16", "2014-10-04", "2014-10-24", "2013-12-26", "2014-04-26", "2014-07-05", "2014-08-19", "2014-09-14", "2014-10-05", "2014-10-26", "2014-01-01", "2014-04-27", "2014-07-16", "2014-08-20", "2014-09-16", "2014-10-07", "2014-01-15", "2014-05-10", "2014-07-24", "2014-08-24", "2014-09-17", "2014-10-08", "2014-10-28", "2014-01-16", "2014-05-12", "2014-07-25", "2014-08-26", "2014-09-18", "2014-10-09", "2014-10-29", "2014-01-26", "2014-05-22", "2014-07-26", "2014-08-27", "2014-09-20", "2014-10-10", "2014-10-30", "2014-02-03", "2014-05-27", "2014-07-27", "2014-08-28", "2014-09-22", "2014-10-11", "2014-10-31", "2014-02-08", "2014-05-30", "2014-09-01", "2014-09-23", "2014-10-12", "2014-11-01", "2014-02-10", "2014-05-31", "2014-07-29", "2014-09-04", "2014-09-24", "2014-10-14", "2014-11-05", "2014-02-15", "2014-06-01", "2014-07-30", "2014-09-05", "2014-09-25", "2014-10-15", "", "2014-02-19", "2014-06-03", "2014-08-01", "2014-09-06", "2014-09-26", "2014-02-22", "2014-08-03", "2014-09-07", "2014-09-28", "2014-10-17", "2014-02-28", "2014-06-11", "2014-08-05", "2014-09-08", "2014-09-29", "2014-10-18", "2014-03-18", "2014-06-16", "2014-08-10", "2014-09-09", "2014-09-30", "2014-10-20", "2014-04-06", "2014-06-17", "2014-08-12", "2014-09-10", "2014-10-02", "2014-10-21", "2014-04-13", "2014-06-22", "2014-08-13", "2014-09-11", "2014-10-03", "2014-10-22"]

for file in file_list:

    subdir = (rootdir + "/" + file)
    
    os.chdir(subdir)
    os.system('rm -r item')
    os.system('rm -r itemimgs')
    os.system('rm -r listing')
    os.system('rm -r send_message')
    os.system('rm -r stars')
    os.system('rm n.png')
    os.system('rm settings')
    os.system('rm st.css')
    os.system('rm vendor_guide.html')
    os.system('rm withdraw')
    os.system('rm btcico.png')
    os.system('rm login')
    os.system('rm register')
    os.system('rm listing.1')
    os.system('rm listing.2')
    os.system('rm listing.3')
    os.system('rm listing.4')
    os.system('rm listing.5')
    os.system('rm profile.1')
    os.system('rm profile.2')
    os.system('rm profile.3')
    os.system('rm profile.4')
    os.chdir(rootdir)

#Script errors at the end but completes what is needed.