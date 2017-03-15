# Determine the price of consuming electric

while True:
    try:
        ConsumeValue = int(input("Kilowatt has been used: "))
    except ValueError:
        print("Please, retype the value: ")
        continue
    else:
        break

ElectricPrice = 0

if 0 <= ConsumeValue < 100:
    ElectricPrice = 1242 * ConsumeValue
elif 100 <= ConsumeValue < 150:
    ElectricPrice = 1242 * 100 + 1369 * (ConsumeValue - 100)
elif 150 <= ConsumeValue < 200:
    ElectricPrice = 1242 * 100 + 1369 * 50 + 1734 * (ConsumeValue - 150)
elif 200 < ConsumeValue:
    ElectricPrice = 1242 * 100 + 1369 * 50 + 1734 * 50 + 1877 * (ConsumeValue - 200)

print("Electric Price is: {}  ".format(ElectricPrice))
