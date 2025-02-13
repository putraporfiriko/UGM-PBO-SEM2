temp = float(input("Enter the temperature: "))

match temp:
    case _ if temp < 0:
        print("Freezing")
    case _ if temp < 20:
        print("Very Cold")
    case _ if temp < 30:
        print("Cold")
    case _ if temp < 40:
        print("Warm")
    case _:
        print("Hot")
