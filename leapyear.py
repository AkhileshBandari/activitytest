year=int(input("Enter a Year:"))
if year%4==0 and year%100!=0 :
    print(f"The {year} is Leap year")
else:
    print(f"the {year} is not leap year")