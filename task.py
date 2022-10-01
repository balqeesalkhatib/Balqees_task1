#------------- length-----------
len=int(input("input your length"))
#my length is 173
if len  >= 170 :
     print("tall")
else:
     print("short")
#------------- leap year-----------
# the year number must be divisible by four, except for end of the end of the century should divisable by 400
year= 2022
if (year % 400 == 0) and (year % 100 == 0):
        print("2022 is leap year")
elif (year % 4 == 0) and (year % 100 != 0) :
        print("2022 is leap year")
else:
    print("2022 is  notleap year")