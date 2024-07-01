def inputFloat(prompt):
    while True:
        try:
            user_input = input(prompt)
            value = float(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a valid floating-point number.")

def testInputFloat():
    print("Testing inputFloat function.")
    
    result = inputFloat("Enter a floating-point number: ")
    print(f"Output: {result}\n")
    
    result = inputFloat("Enter a floating-point number: ")
    print(f"Output: {result}\n")
    
    result = inputFloat("Enter a floating-point number: ")
    print(f"Output: {result}\n")

if __name__ == "__main__":
    testInputFloat()
