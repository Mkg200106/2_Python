#def greet_user():
  #  """Display a simple greeting"""
   # print("Hello!")
#greet_user()

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello {username}!")
greet_user("Martha")
 # This is an infinite loop!
while True:
     print("\nPlease tell me your name:")
f_name = input("First name: ")
l_name = input("Last name: ")
formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")