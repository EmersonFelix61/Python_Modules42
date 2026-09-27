def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def ft_haverst_day(day):
        if day > days:
            print("Harvest time")
            return
        print("Day", day)
        ft_haverst_day(day + 1)

    ft_haverst_day(1)
