#def describe_pet(animal_type, pet_name):
 ##   """Display information about a pet."""
   ### print(f"I have a {animal_type}.")
    
    #print(f"My {animal_type}'s name is {pet_name.title()}")

#describe_pet("tortoise", "junior")
#describe_pet("dog", "tyson")


#describe_pet(animal_type= 'tortoise', pet_name='junior')
#describe_pet(animal_type='dog', pet_name='tyson')

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    
    print("My {animal_type}'s name is {pet_name.title()}")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='hamster', pet_name='harry')
