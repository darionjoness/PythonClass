from functools import reduce

def average(filename):
    with open(filename, 'r') as file:
        numbers = map(float, file)
        total = reduce(lambda x, y: x + y, numbers)
        file.seek(0)
        count = len(list(file))
    return total / count if count != 0 else 0

def main():
    filename = input("Enter the filename: ")
    avg = average(filename)
    print(f"The average is: {avg}")

if __name__ == "__main__":
    main()
