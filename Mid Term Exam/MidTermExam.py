# navigate.py
# Author: Darion Jones
# Semester: Summer 2024
# Due Date: 06/30/2024
# Instructor: Michael Schnell

import string
from collections import Counter

def cleanWord(word):
    return ''.join(char for char in word if char.isalpha())

def main():
    inputFilename = input("Enter the filename: ")
    outputFilename = "Analysis-" + inputFilename
    
    try:
        inputFile = open(inputFilename, 'r')
        lines = inputFile.readlines()
        inputFile.close()
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return
    
    numLines = len(lines)
    numWords = 0
    numChars = 0
    
    words = []

    for line in lines:
        numChars += len(line)
        cleanedLine = line.translate(str.maketrans('', '', string.punctuation + string.digits))
        lineWords = cleanedLine.split()
        words.extend(lineWords)
    
    cleanedWords = [cleanWord(word) for word in words]
    wordCounter = Counter(cleanedWords)
   
    uniqueWords = {word: count for word, count in wordCounter.items() if count > 0}
    numUniqueWords = len(uniqueWords)
 
    wordPairs = zip(cleanedWords, cleanedWords[1:])
    wordPairCounter = Counter(wordPairs)
  
    frequentWordPairs = {pair: count for pair, count in wordPairCounter.items() if count > 1}
    numFrequentWordPairs = len(frequentWordPairs)
   
    numWords = sum(wordCounter.values())
    totalWordLength = sum(len(word) for word in cleanedWords)
    avgWordLength = totalWordLength / numWords if numWords else 0
    
    totalUniqueWordLength = sum(len(word) for word in uniqueWords)
    avgUniqueWordLength = totalUniqueWordLength / numUniqueWords if numUniqueWords else 0
 
    outputFile = open(outputFilename, 'w')
   
    outputFile.write(f"Number of lines: {numLines}\n")
    outputFile.write(f"Number of words: {numWords}\n")
    outputFile.write(f"Number of characters: {numChars}\n")
    
    print(f"Number of lines: {numLines}")
    print(f"Number of words: {numWords}")
    print(f"Number of characters: {numChars}")
  
    for word in sorted(uniqueWords):
        outputFile.write(f"{word} ({uniqueWords[word]})\n")
 
    outputFile.write("\nTwo-word pairs that appear more than once:\n")
    for pair in sorted(frequentWordPairs):
        outputFile.write(f"{pair[0]} {pair[1]} ({frequentWordPairs[pair]})\n")
  
    print("Two-word pairs that appear more than once:")
    for pair in sorted(frequentWordPairs):
        print(f"{pair[0]} {pair[1]} ({frequentWordPairs[pair]})")
 
    outputFile.write("\nAdditional Statistics:\n")
    outputFile.write(f"Total number of words: {numWords}\n")
    outputFile.write(f"Average word length: {avgWordLength:.2f}\n")
    outputFile.write(f"Number of unique words: {numUniqueWords}\n")
    outputFile.write(f"Average length of unique words: {avgUniqueWordLength:.2f}\n")
    outputFile.write(f"Number of two-word pairs with frequency > 1: {numFrequentWordPairs}\n")
   
    print("Additional Statistics:")
    print(f"Total number of words: {numWords}")
    print(f"Average word length: {avgWordLength:.2f}")
    print(f"Number of unique words: {numUniqueWords}")
    print(f"Average length of unique words: {avgUniqueWordLength:.2f}")
    print(f"Number of two-word pairs with frequency > 1: {numFrequentWordPairs}")
    
    outputFile.close()

if __name__ == "__main__":
    main()
