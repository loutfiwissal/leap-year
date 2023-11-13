def leapyear(y):
     if y%4==0 or y%400==0:
          c="this year is a leap year. "
     else :
          c="this year isn't a leap year"
     return(c)
def century(y): 
     for i in range(y-100,y):
          leapyear(i)
          if leapyear(i)=="this year is a leap year. ":
               print(i)
y=int(input("type a year :"))
print(leapyear(y))
print(century(y))