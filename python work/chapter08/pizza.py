def make_pizza(size,*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
print("\nMaking a pizza with the following toppings:")
#print(f"\nMaking a {size}-inch pizza with the following toppings:")
#for topping in toppings:
 #       print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")