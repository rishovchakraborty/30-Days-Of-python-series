def greet(name, location):
    # Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)



# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "rishov", "location": "Kolkata"}

greet(**my_dict)

# The ** operator unpacks the dictionary, passing its key-value pairs 
# as keyword arguments to the function.