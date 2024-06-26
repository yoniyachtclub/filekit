import os
import shutil
import json
import re
import zipfile
import csv

#STEP 1, locate all the files with mp3, put into one dictionary
#STEP 2, add all filepaths with that filename as a value of the dictionary
#STEP 3, choose the best filepath based on hierarchy of organization and delete the files at the other paths
    #Organization system is based on keeping certain folder schemas and date modified
        #Manual: move crates into iTunes
    #Keep everything that is in the iTunes Library (organized by album and artist)
    #/Macintosh HD/Users/meghnamahadevan/Music/Music/Media
    #move everything to one folder that I want to delete


#STEP 4, dump the rest of the files into a folder which needs to be organized
#STEP 5, check if there is anything left behind (not in the big folder)

#XML

#DEFINE GLOBAL VARIABLES
numDuplicates = 0 #Total number of duplicates
totalMusicFiles = 0
musicLibrary = {}

#STEP 1, locate all the files with mp3, put into one dictionary
def CompileLibrary(pathToSearch):
    global totalMusicFiles
    global musicLibrary
            # for all filesinthecomputer, append all files in the computer which contain.mp3 to allmpthrees list
    for root, dirs, files in os.walk(pathToSearch):
        for filename in files:
            # with zipfile.ZipFile('data.zip', 'r') as zipobj:
            if os.path.splitext(filename)[1] in [".mp3", ".mp4", ".m4a", ".wav", ".flac"]:
                totalMusicFiles = totalMusicFiles + 1
            # yield os.path.join(root, filename)
    #allfiles list sorted by name and date modified, most recent date modified first, size of file, most recent date added first
                if filename in musicLibrary.keys():
                    pass
                else:
                    musicLibrary[filename] = []
                    #STEP 2, add all filepaths with that filename as a value of the dictionary
                musicLibrary[filename].append(root) 

#STEP 2, move the to-be-deleted duplicates into a folder to be reviewed and deleted
def DeleteDuplicates(library):
    global numDuplicates #Total number of duplicates
    src = ""
    keepDest = "./keep"
    deleteDest = "./delete"

    #create keep and delete folders
    if not os.path.exists('./keep'):
        os.makedirs('keep')
    if not os.path.exists('./delete'):
        os.makedirs('delete')

   #try: 
    for filename in library:  #every filename in the library
        listpaths = library[filename] #index for filename
        attributesArray = [] #array with attributes for each version of this file


    #Organization system is based on keeping certain folder schemas or choosing the most recent date modified
        if len(listpaths) > 1: #THESE ARE THE ONES WITH DUPLICATES
            numDuplicates = numDuplicates + 1
            maxFileSize = 0
            mostRecentlyModified = 0



            #Compare the file size, date modified,  

            for fp in listpaths:
                fullPath = fp + '/' + filename
                attributes = getFileAttributes(fullPath)
                 #LOGIC: BIGGEST FILE SIZE ?
                if attributes["fileSize"] > maxFileSize: 
                    maxFileSize = attributes["fileSize"]
                    src = attributes["filePath"] # current contender for file to keep
            if (getFileAttributes[src])["keep"] != 1:
                    (getFileAttributes[src])["keep"] = 2
            

                    mostRecentlyModified = attributes["lastModified"] 
                    
                
                    elif attributes["fileSize"] == maxFileSize:
                        if attributes["lastModified"] > mostRecentlyModified:
                            continue #add code here
                else:
    

             #Go through all the filepaths for that file and move this file to delete folder
            for fp in listpaths: 
                fullPath = fp + '/' + filename
                attributes = getFileAttributes(fullPath)

                # check if in itunes - if yes, keep
            attributesArray.sort(key=sortByFileSize) # https://www.w3schools.com/python/ref_list_sort.asp
            print ("sorted by file size:")
            print (attributesArray)
                    
                
            
            #TODO move rest to delete folder
        else: 
            src = listpaths[0] + '/' + filename
            attributes = getFileAttributes(src)
            # if not attributes["iniTunes"] : # if no duplicates and not in itunes, move to keep folder.
            #shutil.move(src,keepDest)
            
    return

#Create dictionary to describe each file
def getFileAttributes(filePath) :
    attributes = {
        "filePath" : filePath,
        "iniTunes": 0,
        "YONI2COPY": 0,
        "lastModified" : 0,
        "lastOpened" : 0,
        "fileSize" : 0, #size in bytes
        "lastOpenedRekordBox" : 0, #date
        "src" : "canifindoutwhereitsdownloadedfrom", 
        "keep" : 0
    }
# this all needs test
    filePath = filePath.lower()
    # print(filePath)
    if "meghnamahadevan/music/music/media.localized" in filePath:
        attributes["iniTunes"] = 1
    if "YONI2" in filePath: 
        attributes["YONI2COPY"] = 1
    attributes["lastModified"] = os.stat(filePath).st_mtime
    attributes["lastOpened"] = os.stat(filePath).st_atime
    attributes["fileSize"] = os.path.getsize(filePath)
    return attributes 
    #re rekordbox - check https://pypi.org/project/pyrekordbox/
                #ATTRIBUTES
                # iniTunes = #yes/no - in file path 
                # recentlymodified = os.stat() #date
                # recentlyopened= #date
                # filesize = #size
                # rekordbox = #date
                # source = #canifindoutwhereitsdownloadedfrom?
    print (filePath)
    print (attributes)
    return attributes


# functions for sorting the array of duplicates
def sortByFileSize(filename) : 
    # check if first two+ elements are same file size. if no, continue with move operation
    maxFileSize = 0
    listpaths = musicLibrary[filename]
    for filepath in listpaths:
        attributesdict = getFileAttributes(filepath)   
        if attributesdict["fileSize"] > maxFileSize:
            attributesdict
        elif maxFileSize = attributesdict["fileSize"]
        else:
            pass
            subAttr = [] #create array with attributes of any same-sized files
            for attr in attributesArray:
                if attr["fileSize"] == maxFileSize:
                    subAttr.append(attr)
                else:
                    break
            # if any of the files are the same size as the max, re-sort those by last modified
            if len(subAttr) > 1:        
                subAttr.sort(key=sortByLastModified)
                src = subAttr[0]["filePath"] # choose most recently modified to keep
            else:
                src = attributesArray[0]["filePath"]
            shutil.move(src,keepDest)

    return element["fileSize"]



def sortByLastModified(element) : 
    return element["lastModified"]

####




try:
    with open('mp4dictionary.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile)
        writer.writeheader()
        writer.writerows(musicLibrary)
except:
    with open('mp6.csv', 'w') as f:
        for key in musicLibrary.keys():
            f.write("%s, %s\n" % (key, musicLibrary[key]))



###RUNNING FUNCTIONS
# search computer
CompileLibrary('/users/meghnamahadevan/documents/allmusic')
DeleteDuplicates(musicLibrary)
print("WE HAVE " + str(numDuplicates) + " DUPLICATES TO DEAL WITH OUT OF " + str(totalMusicFiles) + " FILES")
# search USB(s)
# CompileLibrary('path/to/usb')


#TO DO LIST
#test which ones will be deleted
#move deleted decisions to one folder
#manually delete
#build xml situation
#     ORGANIZE THE DUMP FOLDER
#     export all itunes playlists into text files
#     Name folders based off of playlists

