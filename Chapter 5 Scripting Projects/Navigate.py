def loadFile(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return []

def main():
    filename = input("Enter the filename: ")
    lines = loadFile(filename)
    
    if not lines:
        return
    
    numLines = len(lines)
    
    while True:
        print(f"The file contains {numLines} lines.")
        try:
            lineNumber = int(input("Enter a line number (0 to quit): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        if lineNumber == 0:
            break
        elif 1 <= lineNumber <= numLines:
            print(f"Line {lineNumber}: {lines[lineNumber - 1].strip()}")
        else:
            print(f"Please enter a number between 1 and {numLines}.")

if __name__ == "__main__":
    main()
