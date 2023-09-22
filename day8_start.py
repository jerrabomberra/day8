# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet(location,name='joe'):
    print("good day {name}")
    print(f"Thursday is nice at {location}" )
    return name.title(), location

# name=input("Name please : ")
print(f"Hello" , greet('London'))