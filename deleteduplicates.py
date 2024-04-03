import os
import shutil
import json
import re


#STEP 1, locate all the music files, put into one dictionary - DONE - needs test
#STEP 2, add all filepaths with that filename as a value of the dictionary - DONE - needs test
#STEP 3, add all the filepaths as a key to a dictionary, with the value being a set of attributes for the file at that path - TODO
#STEP 4, choose the best filepath based on hierarchy of organization and delete the files at the other paths - TODO
    #Organization system is based on keeping certain folder schemas and date modified
        #Manual: move crates into iTunes
    #Keep everything that is in the iTunes Library (organized by album and artist)
    #/Macintosh HD/Users/meghnamahadevan/Music/Music/Media
    #move everything to one folder that I want to delete
#STEP 5, dump the rest of the files into a folder which needs to be organized - TODO
#STEP 6, check if there is anything left behind (not in the big folder) - TODO

#XML
#???????

#DEFINE GLOBAL VARIABLES
numDuplicates = 0 #Total number of duplicates
totalMusicCount = 0

#STEP 1, locate all the files with mp3, put into one dictionary
def CompileLibrary():
    global totalMusicCount #maybe change this to totalMusic, because you're checking for all music filetypes and not just mp3
    musicLibraryByFileName = {} 
    musicLibraryWithAttributes = {}
    print ("hi")
    for (root, dirs, files) in os.walk('/Users/meghnamahadevan/Documents/', topdown=False):
        print("ROOT" + str(root))
        print("ALLGOOD" + str(root) + "DIRS" + str(dirs) + "FILES" + str(files))
        #Documents has CRATES, yoni2backup is paused
        #Music has itunes
        for filename in files:
            if os.path.splitext(filename)[1] in [".mp3", ".mp4", ".m4a", ".wav", ".flac"]:
                print(filename)
                totalMusicCount = totalMusicCount + 1

                #adding to musicLibraryWithAttributes dictionary - TODO add a separate function to be called here that gets the attributes of a file
                print('this is where we add to this dictionary with attributes')

                #adding to musicLibraryByFilename dictionary
                if filename in musicLibraryByFileName.keys():
                    pass
                else:
                    musicLibraryByFileName[filename] = []
                    #STEP 2, add all filepaths with that filename as a value of the dictionary
                    musicLibraryByFileName[filename].append(root) 
                    print(root)
    return musicLibraryByFileName




def deletedDuplicates(library):
    global numDuplicates #Total number of duplicates
  #  try: 
    for filename in library: 
        listpaths = library[filename] #index for filename
#STEP 3, choose the best filepath based on hierarchy of organization
    #Organization system is based on keeping certain folder schemas or choosing the most recent date modified
        if len(listpaths) > 1: #THESE ARE THE ONES WITH DUPLICATES
            #  print(listpaths)
            # print ("duplicate", filename)
            numDuplicates = numDuplicates + 1
            for fp in listpaths:
                fullPath = fp + '/' + filename
                fileAttributes = getFileAttributes(fullPath)
   # except:
 #       pass
                   # print (fileAttributes)
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
#                         musicLibraryByFileName[filename] = filepath
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
#             musicLibraryByFileName[filename]= filepathstr
            


#     ORGANIZE THE DUMP FOLDER

#     export all itunes playlists into text files
#     Name folders based off of playlists

def getFileAttributes(filePath) :
    attributes = {
        "iniTunes": 0,
        "YONI2COPY": 0,
        "lastModified" : 0,
        "lastOpened" : 0,
        "fileSize" : 0, #size in bytes
        "lastOpenedRekordBox" : 0, #date
        "src" : "canifindoutwhereitsdownloadedfrom"
    }
# this all needs test
    
    if "/meghnamahadevan/Music/Music/Media" in filePath:
        attributes["iniTunes"] = 1
    if "YONI2" in filePath: 
        attributes["YONI2COPY"] = 1
    attributes["lastModified"] = "Modification time: {}".format(os.stat(filePath).st_mtime)
    attributes["lastOpened"] = "Last accessed time: {}".format(os.stat(filePath).st_atime)
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


###RUNNING FUNCTIONS

testdictionary = CompileLibrary()
print("test dictionary")
print(testdictionary)
deletedDuplicates(testdictionary)
print("WE HAVE " + str(numDuplicates) + " DUPLICATES TO DEAL WITH OUT OF " + str(totalMusicCount) + " FILES")


#TO DO LIST
#test iTunes feature, is this possible
#double check file priorities
#test which ones will be deleted
#move deleted decisions to one folder
#manually delete
#build xml situation


