YearNow = input("What year is it now? (ex: 2020)")
MonthNow = input("What Month is it now? (ex: 10)")
InputYear =input("Your year of birth :")
InputMonth = input("Your Month of birth :")

Year = int(YearNow)
Month = int(MonthNow)

def AgeCal():
    if int(InputMonth) > 12 :
        print(" ERROR: 404, Don't try to crash me :)")
    if int(InputYear) > int(Year) :
        print(" ERROR: 404, Don't try to crash me :)")
    if int(InputMonth) > int(Month) and int(InputMonth) < 12 :
        BirthYear = (int(Year) - int(InputYear)) - 1
        BirthMonth = (int(Month) - 12) + (int(InputMonth))
        print("You are",BirthYear, "Years old","and",BirthMonth,"Months old.")
    if int(InputMonth) <= int(Month) and int(InputMonth) < 12 :
        BirthMonth = (int(Month) - int(InputMonth))
        BirthYear = (int(Year) - int(InputYear))
        print("You are", BirthYear,"Years old","and", BirthMonth, "Months old.")


AgeCal()
