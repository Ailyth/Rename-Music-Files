#%%
import os

def GetMusicFilesOnly(fileList):
    musicOnlyFileList = []


    #show result
    for fileName in fileList:
        if ((".mp3" in fileName) or (".ogg" in fileName)
                or (".flac" in fileName) or (".m4a" in fileName)
                or (".wav" in fileName) or (".aac" in fileName)):
            musicOnlyFileList.append(fileName)
    for fileName in musicOnlyFileList:
        print (fileName)

    print("End of GetMusicFilesOnly() \n")
    CheckMusicFileNames(musicOnlyFileList)


def CheckMusicFileNames(musicOnlyFileList):
    badMusicFileNames = []
    index = 1

    for fileName in musicOnlyFileList:
        trackNumber = '0' + str(index) + '.'
        if (trackNumber not in fileName):
            badMusicFileNames.append(fileName)
        index = index + 1

    #show result
    for fileName in badMusicFileNames:
        print (fileName)
    print("End of CheckMusicFileNames() \n")
    TrimFileNames(badMusicFileNames)

def TrimFileNames(badMusicFileNames):
    trimmedFileNames = []
    index = 1

    for fileName in badMusicFileNames:
        trackNumber = '0' + str(index)
        result = fileName.find(trackNumber)
        print (result)
        fileName = fileName[result:]
        trimmedFileNames.append(fileName)
        index = index + 1

    #show result
    for fileName in trimmedFileNames:
        print (fileName)
    print("End of TrimFileNames() \n")

    # AddDotAfterNumber(trimmedFileNames)

# def AddDotAfterNumber(trimmedFileNames):


fileList = os.listdir()
print (fileList)
GetMusicFilesOnly(fileList)

# %%
