initialHeight = float(input("Enter the height from which the ball is dropped: "))
bouncinessIndex = float(input("Enter the bounciness index of the ball: "))
numberOfBounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

totalDistance = 0
currentHeight = initialHeight

for _ in range(numberOfBounces):
   
    totalDistance += currentHeight
    
    currentHeight *= bouncinessIndex
    
    totalDistance += currentHeight

print(f"The total distance traveled by the ball is {totalDistance} feet.")
