f = open("vehicle.txt", "w")

#Program Description
""" Program created by Broghan Fields
    Car Sales Program. User chooses the car and
    specifications. Program returns the price
    of the car. """

print("\nWelcome to the car shop.")

#constants
total = 0.00
carType = ""
carModels = ["2 Door", "2 Door Sports", "4 Door", "SUV", "Truck"]
engineType = ["4 Cylinder", "4 Cylinder Hybrid", "4 Cylinder Electric", "6 Cylinder", "6 Cylinder Hybrid", "8 Cylinder"]
baseModelPricing = [12000, 16000, 18000, 22000, 25000]

#truck options
def printCarEngineOptions():
  print("Option |     Description    |   Add    ")
  print("  1    |     4 Cylinder     | No Charge")
  print("  2    | 4 Cylinder Hybrid  |  $5,000  ")
  print("  3    | 4 Cylinder Electric|  $6,000  ")
  print("  4    |     6 Cylinder     |  $7,000  ")
  print("  5    |  6 Cylinder Hybrid | $10,000  ")
  print("  6    |     8 Cylinder     | $13,000  ")

#car options
def printTruckEngineOptions():
  print(" Option |    Description    |   Add   |")
  print("  1     |     6 Cylinder    | $7,000  |")
  print("  2     | 6 Cylinder Hybrid | $10,000 |")
  print("  3     |    8 Cylinder     | $13,000 |")

#warranty options
def extrasExtWarr():
  extra2 = input("Would you like to add the Extented Warranty? (y)/(n) ")
  extra2 = extra2.lower()
  if extra2 == "n":
    print("You don't need it anyway!")
    return 0
  elif extra2 == "y":
    print("You chose to add an extended warranty for",'${:,.2f}'.format(1500))
    return 1500
  else:
    while extra2 != "y" or extra2 != "n":
      extra2 = input("Please enter (y)/(n) only. ")
      extra2 = extra2.lower()
      if extra2 == "y" or extra2 == "n":
        break

#luxury option
def extrasLux():
  print("The luxury option includes heated seats, GPS, and electric windows for $3,000.")
  extra1 = input("Would you like to add the Luxury Option? (y)/(n) ")
  extra1 = extra1.lower()
  if extra1 == "n":
    print("Luxury Option not chosen")
    return 0
  elif extra1.lower() == "y":
    print("You chose to add a luxury package for",'${:,.2f}'.format(3000))
    return 3000
  while extra1 != "y" or extra1 != "n":
    extra1 = input("Please enter (y)/(n) only. ")
    extra1 = extra1.lower()
    if extra1 == "y" or extra1 == "n":
      break

#totals function and receipt
def figureCarTotal(car, carEngine,carEnginePrice, carEngineChoice,carPrice,total):
  luxury = 0
  warranty = 0
  print("You have chosen a", car, "car with a", carEngine, "engine for", '${:,.2f}'.format(total))
  luxury = extrasLux()
  warranty = extrasExtWarr()
  if luxury > 0:
    luxuryPurchase = "yes"
    luxury = 3000
    total+=3000
  else:
    luxuryPurchase = "no"
  if warranty > 0:
    extWarrantyPurchase = "yes"
    warranty = 1500
    total+=1500
  else:
    extWarrantyPurchase = "no"
  print("|    Car Summary    |     Description      |   Cost  |")
  print("|     Car Model    "     , "      ", car, "       " ,'${:,.2f}'.format(carPrice))
  print("|    Engine Type      ",carEngine, "     ", '${:,.2f}'.format(carEnginePrice))
  print("|    Luxury Package         ",luxuryPurchase,"       " ,'${:,.2f}'.format(luxury))
  print("|  Extended Warranty        ",extWarrantyPurchase, "       " '${:,.2f}'.format(warranty))
  print("|  Total Purchase Price                 ", '${:,.2f}'.format(total))

#main function
def chooseCar():
  print("|Choices     |   1   | |   2   | |    3   | |   4   | |   5   |")
  print("|             2 Door    Sports     4 Door      SUV      Truck |")
  print("|Base Price  $12,000    $16,000    $18,000   $22,000   $25,000|")
  print("\n")
  carType = input("Choose your car type from the menu. Please enter 1, 2, 3, 4, or 5. ")
  if carType == "1":
    car = carModels[0]
    f.write(car)
    carPrice = baseModelPricing[0]
    f.write(str(carPrice))
    carEngine = ""
    carEnginePrice = 0
    total = carPrice
    f.write(str(total))
    print("\nYou chose a", car, " for ", '${:,.2f}'.format(total))
    print("The engine options for a ",car, " are listed below\n")
    printCarEngineOptions()
    print("Would you like to add an engine option? ")
    carEngineChoice = input("Enter 1, 2, 3, 4, 5, or 6. ")
    if carEngineChoice == "1":
      carEngine = "4 Cylinder"
      f.write(carEngine)
      carEnginePrice = 0
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
    elif carEngineChoice == "2":
      carEngine = "4 Cylinder Hybrid"
      f.write(carEngine)
      carEnginePrice = 5000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "3":
      carEngine = "4 Cylinder Electric"
      f.write(carEngine)
      carEnginePrice = 6000
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "4":
      carEngine = "6 Cylinder"
      f.write(carEngine)
      carEnginePrice = 7000
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "5":
      carEngine = "6 Cylinder Hybrid"
      f.write(carEngine)
      carEnginePrice = 10000
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "6":
      carEngine = "8 Cylinder"
      f.write(carEngine)
      carEnginePrice = 13000
      total = total + carEnginePrice
      f.write(str(total))

    figureCarTotal(car, carEngine, carEnginePrice, carEngineChoice, carPrice, total)


  elif carType == "2":
    car = carModels[1]
    f.write(car)
    carPrice = baseModelPricing[1]
    f.write(str(carPrice))
    carEngine = ""
    carEnginePrice = 0
    total = carPrice
    f.write(str(total))
    print("\nYou chose a", car, " for ", '${:,.2f}'.format(total))
    print("The engine options for a ",car, " are listed below\n")
    printCarEngineOptions()
    print("Would you like to add an engine option? ")
    carEngineChoice = input("Enter 1, 2, 3, 4, 5, or 6. ")
    if carEngineChoice == "1":
      carEngine = "4 Cylinder"
      f.write(carEngine)
      carEnginePrice = 0
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "2":
      carEngine = "4 Cylinder Hybrid"
      f.write(carEngine)
      carEnginePrice = 5000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "3":
      carEngine = "4 Cylinder Electric"
      f.write(carEngine)
      carEnginePrice = 6000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "4":
      carEngine = "6 Cylinder"
      f.write(carEngine)
      carEnginePrice = 7000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "5":
      carEngine = "6 Cylinder Hybrid"
      f.write(carEngine)
      carEnginePrice = 10000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "6":
      carEngine = "8 Cylinder"
      f.write(carEngine)
      carEnginePrice = 13000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    figureCarTotal(car, carEngine, carEnginePrice, carEngineChoice, carPrice, total)

  elif carType == "3":
    car = carModels[2]
    f.write(car)
    carPrice = baseModelPricing[2]
    f.write(str(carPrice))
    carEngine = ""
    carEnginePrice = 0
    total = carPrice
    f.write(str(total))
    print("\nYou chose a", car, " for ", '${:,.2f}'.format(total))
    print("The engine options for a ",car, " are listed below\n")
    printCarEngineOptions()
    print("Would you like to add an engine option? ")
    carEngineChoice = input("Enter 1, 2, 3, 4, 5, or 6. ")
    if carEngineChoice == "1":
      carEngine = "4 Cylinder"
      f.write(carEngine)
      carEnginePrice = 0
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "2":
      carEngine = "4 Cylinder Hybrid"
      f.write(carEngine)
      carEnginePrice = 5000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "3":
      carEngine = "4 Cylinder Electric"
      f.write(carEngine)
      carEnginePrice = 6000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "4":
      carEngine = "6 Cylinder"
      f.write(carEngine)
      carEnginePrice = 7000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "5":
      carEngine = "6 Cylinder Hybrid"
      f.write(carEngine)
      carEnginePrice = 10000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "6":
      carEngine = "8 Cylinder"
      f.write(carEngine)
      carEnginePrice = 13000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    figureCarTotal(car, carEngine, carEnginePrice, carEngineChoice, carPrice, total)

  elif carType == "4":
    car = carModels[3]
    f.write(car)
    carPrice = baseModelPricing[3]
    f.write(str(carPrice))
    carEngine = ""
    carEnginePrice = 0
    total = carPrice
    f.write(str(total))
    print("\nYou chose a", car, " for ", '${:,.2f}'.format(total))
    print("The engine options for a ",car, " are listed below\n")
    printCarEngineOptions()
    print("Would you like to add an engine option? ")
    carEngineChoice = input("Enter 1, 2, 3, 4, 5, or 6. ")
    if carEngineChoice == "1":
      carEngine = "4 Cylinder"
      f.write(carEngine)
      carEnginePrice = 0
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "2":
      carEngine = "4 Cylinder Hybrid"
      f.write(carEngine)
      carEnginePrice = 5000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "3":
      carEngine = "4 Cylinder Electric"
      f.write(carEngine)
      carEnginePrice = 6000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "4":
      carEngine = "6 Cylinder"
      f.write(carEngine)
      carEnginePrice = 7000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "5":
      carEngine = "6 Cylinder Hybrid"
      f.write(carEngine)
      carEnginePrice = 10000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "6":
      carEngine = "8 Cylinder"
      f.write(carEngine)
      carEnginePrice = 13000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    figureCarTotal(car, carEngine, carEnginePrice, carEngineChoice, carPrice, total)

  elif carType == "5":
    car = carModels[4]
    f.write(car)
    carPrice = baseModelPricing[4]
    f.write(str(carPrice))
    carEngine = ""
    carEnginePrice = 0
    total = carPrice
    f.write(str(total))
    print("\nYou chose a", car, " for ", '${:,.2f}'.format(total))
    print("The engine options for a ",car, " are listed below\n")
    printTruckEngineOptions()
    print("Would you like to add an engine option? ")
    carEngineChoice = input("Enter 1, 2, or 3. ")
    if carEngineChoice == "1":
      carEngine = "6 Cylinder"
      f.write(carEngine)
      carEnginePrice = 7000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "2":
      carEngine = "6 Cylinder Hybrid"
      f.write(carEngine)
      carEnginePrice = 10000
      f.write(str(carEnginePrice))
      total = total + carEnginePrice
      f.write(str(total))
    elif carEngineChoice == "3":
      carEngine = "8 Cylinder"
      f.write(carEngine)
      carEnginePrice = 13000
      f.write(str(carEnginePrice))
      total= total + carEnginePrice
      f.write(str(total))
    figureCarTotal(car, carEngine, carEnginePrice, carEngineChoice, carPrice, total)

  #loop program option
  changeOrder = input("Would you like to order another car? (y)/(n) \n")
  changeOrder = changeOrder.lower()
  if changeOrder == "n":
    print("Thanks for stopping by!")
  else:
    chooseCar()

  #close file
  f.close()

#start program
chooseCar()
