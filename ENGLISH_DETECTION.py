#Self-dev English Detector module
#you need to download an English dictionary Text File to use this module
#go to google or any search engine and download an English Dictionary File
#a one you can use :

#import eng
#eng.isEnglish(message) ; will return false or true.
#eng.DictLoader() ; will ask you for a the English dictionary file name then returns a dictionary that contains all the words in that dictionary file.
#eng.countWords() ; will return the percentage of English words in the entered text .
#eng.englishWords() ; will return the english words in the entered text in a list.

Englishletters = "abcdefghijklmnopqrstuvwxyz"
fullEnglishLetters = Englishletters + " \n\t"

def DictLoader(): #loads the dictionary text File, if the function isn't called the program will automatically set the language to English.
    englishWords = {}
    dictFileName = input("enter the dictionary file name (make sure to specify the whole path or copy the dictionary file into the python32 folder and just type the File's name) : ")
    dictFile = open(dictFileName)
    EnglishWords = dictFile.read()
    for word in EnglishWords.split('\n'):
        englishWords[word] = None
    dictFile.close()
    return englishWords

def countWords(text): #this function will remove all the non-letter characters and count how many real word(not gibberish) in the provided text.
    chars = []
    counter = 0
    for char in text:
        if char in fullEnglishLetters:
            chars.append(char)
    nonLetters = ''.join(chars)
    if chars == []:
        return 0
    wordsDict = DictLoader()
    for word in nonLetters.split():
        if word in wordsDict:
            counter += 1
    return (counter/len(nonLetters.split())) * 100


def isEnglish(text , percantage = 35 , letterPercentage = 5):
    wordsMatch = countWords(text) >= percantage
    chars = []
    for char in text:
        if char in fullEnglishLetters:
            chars.append(char)
    nonLetters = ''.join(chars)
    lettersPercentage = len(nonLetters)/len(text) * 100
    lettersMatch = lettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
    
def englishWords(text):
    chars = []
    eng = []
    counter = 0
    for char in text:
        if char in fullEnglishLetters:
            chars.append(char)
    nonLetters = ''.join(chars)
    if chars == []:
        return 0
    wordsDict = DictLoader()
    for word in nonLetters.split():
        if word in wordsDict:
            eng.append(word)

    return eng




