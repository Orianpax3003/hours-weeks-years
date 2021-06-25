#pythone programe to calculate total no of hours

print("Enter choice : 1)No of days 2) No of weeks 3) No of years")
i=int(input("choice:"))
if  i==1 :
    d=float(input("No of days:"))
    z=d*24
    print(f"NO of days is {d} therefore total hours is{z}")
elif i==2 :
    W= float(input("No of weeks:"))
    z=W*24*7
    print(f"NO of weeks is {W} therefore total hours is{z}")
elif i==3 :
    Y = float(input("No of years:"))
    z=Y*365*24
    print(f"NO of years is {Y} therefore total hours is {z}")  
else :
    print("INVALID CHOICE!!!!") 






    
    