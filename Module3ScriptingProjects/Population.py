initialPopulation = int(input("Enter the initial number of organisms: "))
growthRate = float(input("Enter the rate of growth (a real number greater than 0): "))
growthPeriod = int(input("Enter the number of hours it takes to achieve this rate: "))
totalHours = int(input("Enter the number of hours during which the population grows: "))


numGrowthPeriods = totalHours // growthPeriod


totalPopulation = initialPopulation * (growthRate ** numGrowthPeriods)


print(f"The predicted total population after {totalHours} hours is {totalPopulation:.0f}.")
