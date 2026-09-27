def ft_water_reminder():
    lastday = input("Days since last watering: ")
    if int(lastday) <= 2:
        print("Plant are fine")
    else:
        print("Water the plants!")
