import os

rootdir = os.getcwd()

#this script removes all other directories that was not "vender" from the
#different dates that Hydra was scraped.This is done because for the time
#being we are only looking at vendor data.

for subdir, dirs, files in os.walk(rootdir):
   for subdir in dirs:
        os.chdir(subdir)
        os.system('rm -r category')
        os.system('rm -r fonts')
        os.system('rm -r font')
        os.system('rm -r images')
        os.system('rm -r style')
        os.system('rm -r sale')
        os.system('rm -r css')
        os.chdir(rootdir)
        
#Script errors at the end but completes what is needed.