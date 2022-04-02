import calendar

def main():
    month , day , year = map(int,input().split( ))
    #print(day,month,year)
    chossen_date = calendar.weekday(year,month,day)
    #print (calendar.TextCalendar().formatyear(year))
    if chossen_date == 0:
        print("MONDAY")
    elif chossen_date == 1:
        print("TUESDAY")
    elif chossen_date == 2:
        print("WEDNESDAY")
    elif chossen_date == 3:
        print("THURSDAY")
    elif chossen_date == 4:
        print("FRIDAY")
    elif chossen_date == 5:
        print("SATURDAY")
    elif chossen_date == 6:
        print("SUNDAY")


    

if __name__ == "__main__":
    main()
