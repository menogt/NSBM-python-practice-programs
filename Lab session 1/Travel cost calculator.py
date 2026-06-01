distance_traveled = float(input("Enter the distance traveled: "))
fe = float(input("Enter Milege per liter: "))
fppl = float(input("How much a fuel liter cost? "))
hc = float(input("Enter your highway charges: "))
fu = float(distance_traveled/fe)
fc = float(fu*fppl)
total_cost = fc+hc

print("The amount of fuel used is ",fu)
print("Fuel Cost is",fc)
print("Highway charges are", hc)
print("Total Cost is", total_cost)
