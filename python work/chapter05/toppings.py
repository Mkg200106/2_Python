#requested_topping= 'mushrooms'
#if requested_topping != 'anchovies':
    #print("Hold the anchovies!")

#requested_toppings = ['mushrooms', 'extra cheese']
#if 'mushrooms' in requested_toppings:
   # print('Adding mushrooms.')
#elif 'pepperoni' in requested_toppings:
#    print('Adding pepperoni.')
#if 'extra cheese' in requested_toppings:
#    print('Adding extra cheese')

#print('Finished making your pizza!')

requested_toppings = ['mushrooms', 'green peppers']

for requested_topping in requested_toppings :
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!")