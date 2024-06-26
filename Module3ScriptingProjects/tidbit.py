purchasePrice = float(input("Enter the purchase price: "))

downPaymentRate = 0.10
annualInterestRate = 0.12  
monthlyPaymentRate = 0.05

downPayment = purchasePrice * downPaymentRate
balance = purchasePrice - downPayment


month = 0
interestRateMonthly = annualInterestRate / 12
maxIterations = 1000  


paymentSchedule = []


while balance > 0 and month < maxIterations:
    month += 1
    interest = balance * interestRateMonthly
    principal = balance * monthlyPaymentRate
    payment = interest + principal
    balance -= payment
    
    
    paymentSchedule.append((month, balance, interest, principal, payment))


print("Month\tTotal Balance\tInterest\tPrincipal\tPayment\tRemaining Balance")


for data in paymentSchedule:
    month, balance, interest, principal, payment = data
    print(f"{month}\t${balance:.2f}\t${interest:.2f}\t${principal:.2f}\t${payment:.2f}\t${balance:.2f}")


if month >= maxIterations:
    print(f"Warning: Maximum number of iterations ({maxIterations}) reached. Consider checking input values for correctness.")
