# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello Glasgow!")

x = float(input("Please enter a value for x: "))
y = float(input("Please enter a value for y: "))
print("\nThe average of x and y is " + str((x+y)/2))

#module = "CSC1009"
module = input("\n\nPlease enter a module: ").lower()

if module == "csc1006":
    print("Mathematics 2")
    
elif module == "csc1007":
    print("Operating Systems")
    
elif module == "csc1008":
    print("Data Structures and Algorithms")
    
elif module == "csc1009":
    print("Object-Oriented Programming")
    
else:
    print("Unknown Module")
print("After switch\n");

for i in range(102, 66, -2):
    print("value of x : " + str(i))