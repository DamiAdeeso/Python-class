#Number 1
print("\n Question 1")
print("Adeeso Oluwadamilola Caleb")
print("11 Landuse Road, MapleWood Estate ,Oko-oba,Lagos")
print("+234804938850")
print("Electronics and Computer Engineering.")

print("\n Question 5")
#No 5
speed = int(70);
time = int(6)
Distance = speed*time
print("Distance covered is "+ str(Distance) + " miles.")
time = int(10)
Distance = speed*time
print("Distance covered is "+ str(Distance) + " miles.")



#No7
print("\n Question 7")
miles_driven = int(input("Input Miles Driven: "))
gallons_used = int(input("Input Number of Gallons Used: "))
mpg = (miles_driven/gallons_used)
print("The vehicle goes ", format(mpg,'.2f') ,  " Miles per Gallon ")

# NO11
print("\n Question 11")
boys_no=int(input("Input Number of Boys In The Class: "))
girls_no = int(input("Input Number of Girls in the Class: "))
total_sum = boys_no+girls_no
boys_percent = (boys_no/total_sum)*100
girls_percent = (girls_no/total_sum)*100
print("The percentage of boys in the class is " ,format((boys_percent),'.2f'),"%",sep="")
print("The percentage of girls in the class is " ,format((girls_percent),'.2f'),"%",sep="")
