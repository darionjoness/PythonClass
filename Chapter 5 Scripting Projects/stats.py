def computeMean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def computeMedian(numbers):
    if not numbers:
        return 0
    sortedNumbers = sorted(numbers)
    n = len(sortedNumbers)
    midpoint = n // 2
    
    if n % 2 == 0:
        return (sortedNumbers[midpoint - 1] + sortedNumbers[midpoint]) / 2
    else:
        return sortedNumbers[midpoint]

def computeMode(numbers):
    if not numbers:
        return 0
    from collections import Counter
    counts = Counter(numbers)
    maxCount = max(counts.values())
    modeValues = [num for num, count in counts.items() if count == maxCount]
    
    if len(modeValues) == 1:
        return modeValues[0]
    else:
        return modeValues

def main():
    testList = [10, 10, 12,13, 14, 14, 14, 15,15, 16]
    
    print(f"List: {testList}")
    print(f"Mean: {computeMean(testList)}")
    print(f"Median: {computeMedian(testList)}")
    print(f"Mode: {computeMode(testList)}")

if __name__ == "__main__":
    main()
