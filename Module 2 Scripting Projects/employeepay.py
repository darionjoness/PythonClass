hourlyWage = float(input("Enter the hourly wage: "))

regularHours = float(input("Enter the total regular hours: "))

overtimeHours = float(input("Enter the total overtime hours: "))

regularPay = hourlyWage * regularHours

overtimePay = overtimeHours * (hourlyWage * 1.5)

totalWeeklyPay = regularPay + overtimePay

print(f"The total weekly pay is ${totalWeeklyPay}")
