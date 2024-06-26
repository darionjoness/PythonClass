sourceFileName = input("Enter the name of the source file: ")
destinationFileName = input("Enter the name of the destination file: ")


sourceFile = open(sourceFileName, 'r')

contents = sourceFile.read()


fileDestination = open(destinationFileName, 'w')
    
fileDestination.write(contents)

print(f"Contents of {sourceFileName} have been copied to {destinationFileName}.")
