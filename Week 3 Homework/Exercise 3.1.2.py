start_day=int(input("write a number for which day you're going on holiday\n"))
lenght=int(input("how many days of holiday\n"))
number=((start_day+lenght)%7)
if number==0:
    print("Monday")
elif number==1:
    print("Tuesday")
elif number==2:
    print("Wednesday")
elif number==3:
    print("Thursday")
elif number==4:
    print("Friday")
elif number==5:
    print("Saturday")
elif number==6:
    print("Sunday")

