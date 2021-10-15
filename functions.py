
#function with parameter

def greet_user(first_name, last_name):
    print(f"Hi There! {first_name} {last_name}")
    print("Welcome Aboard")

#positional arguments
#keyword arguments

print("Start")
greet_user("Sham", "Rehman")
greet_user(last_name="Jo", first_name="Bob")
print("Finish")

