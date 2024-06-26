startingSalary = float(input("Enter the starting salary: "))
percentageIncrease = float(input("Enter the percentage increase per year: "))
numYears = int(input("Enter the number of years in the salary schedule: "))

currentSalary = startingSalary

print("Year\tSalary")

for year in range(1, numYears + 1):
    print(f"{year}\t${currentSalary:.2f}")
    currentSalary += currentSalary * (percentageIncrease / 100)
