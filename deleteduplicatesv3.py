import os
import shutil
import json
import re
import zipfile
import csv

#  i love potatoes



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


def DeleteDuplicates(library):
    global numDuplicates #Total number of duplicates
    src = ""
    keepDest = "./keep"
    deleteDest = "./delete"

    # create keep and delete folders
    if not os.path.exists('./keep'):
        os.makedirs('keep')
    if not os.path.exists('./delete'):
        os.makedirs('delete')

  # try: 
    for filename in library: 
        listpaths = library[filename] #index for filename
        attributesArray = [] #array with attributes for each version of this file

#STEP 3, choose the best filepath based on hierarchy of organization
    #Organization system is based on keeping certain folder schemas or choosing the most recent date modified
        if len(listpaths) > 1: #THESE ARE THE ONES WITH DUPLICATES
            numDuplicates = numDuplicates + 1
            maxFileSize = 0
            mostRecentlyModified = 0
            fileIniTunes = False
         
        

            #Go through all the filepaths for that file
            for fp in listpaths: 
                fullPath = fp + '/' + filename
                attributes = getFileAttributes(fullPath)

               

                #LOGIC: Is it in itunes?
                if attributes["iniTunes"]:
                    fileIniTunes = True #YES it is in itunes
                    attributes["keep"] = 1
                    break

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
            #For this filepath 
                    
                    #move this file to delete folder


                # check if in itunes - if yes, keep
            attributesArray.sort(key=sortByFileSize) # https://www.w3schools.com/python/ref_list_sort.asp
            print ("sorted by file size:")
            print (attributesArray)

            # check if first two+ elements are same file size. if no, continue with move operation
            maxFileSize = attributesArray[0]["fileSize"]
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

            #TODO move rest to delete folder
        else: 
            src = listpaths[0] + '/' + filename
            attributes = getFileAttributes(src)
            # if not attributes["iniTunes"] : # if no duplicates and not in itunes, move to keep folder.
            #     shutil.move(src,keepDest)
            
    return


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
def sortByFileSize(element) : 
    return element["fileSize"]

def sortByLastModified(element) : 
    return element["lastModified"]

###RUNNING FUNCTIONS
# search computer
CompileLibrary('/users/meghnamahadevan/documents/allmusic')
# search USB(s)
# CompileLibrary('path/to/usb')

DeleteDuplicates(musicLibrary)
print("WE HAVE " + str(numDuplicates) + " DUPLICATES TO DEAL WITH OUT OF " + str(totalMusicFiles) + " FILES")


try:
    with open('mp4dictionary.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile)
        writer.writeheader()
        writer.writerows(musicLibrary)
except:
    with open('mp6.csv', 'w') as f:
        for key in musicLibrary.keys():
            f.write("%s, %s\n" % (key, musicLibrary[key]))

#TO DO LIST
#test iTunes feature, is this possible
#double check file priorities
#test which ones will be deleted
#move deleted decisions to one folder
#manually delete
#build xml situation




   # except:
 #       pass
                
                #ATTRIBUTES
                # iniTunes = #yes/no - in file path 
                # recentlymodified = os.stat() #date
                # recentlyopened= #date
                # filesize = #size
                # rekordbox = #date
                # source = #canifindoutwhereitsdownloadedfrom?
                
                #IF THERE IS ONE IN ITUNES
                    #pass

                #IF THERE ARE MULTIPLE IN ITUNES
                    #that's okay

                #IF NONE IN ITUNES
                    #keep the one with with biggest filesize

                    #keep the one with date most recently modified

                
#                 for filepath in pathways #go through and look for crates
#                     if filepath contains "CRATES"
#                         print ("CRATES")
#                         for filepath in pathways
#                             if filepath does not contain crates
#                                 delete
#                         musicLibrary[filename] = filepath
#                     else pass
#                 for filepath in pathways #go through and look for itunes playlist
#                     if filepath #in itunes playlist
#                         print ["Itunes" ]
#                         for filepath in pathways   
#                             if filepath does not contain itunes
#                                 delete
#                     else pass
#             #  any other duplicates, order by date and delete the others    
#             if length(pathways) > 1 and pathways is not a string  ##DUPLICATES_rest of the files
#                 for filepath in pathways[1:]
#                         delete
#                         delete the other files

# #STEP 4, dump the files into a folder which needs to be organized

#                 move into one folder, change filepath
#             else:
#                 pass

#             if length(pathways) > 1 OR pathways is not a string #ANYOTHERS? 
#                 print ("There is something weird", pathways)
#             else:
#                 pass
            

#             filepathstr = pathways[0]
#             musicLibrary[filename]= filepathstr
            


#     ORGANIZE THE DUMP FOLDER

#     export all itunes playlists into text files
#     Name folders based off of playlists
