#def get_formatted_name(first_name, last_name) :
   ##3 """Return a full name, neatly formatted."""
   # full_name = f"{first_name} {last_name}"
   ## return full_name.title()

3#musician = get_formatted_name ('jimi', 'hendrix')
#print(musician)

def get_formatted_name (first_name, last_name, middle_name= ''):
    """Return a full name, neatly formatted"""
    if middle_name: 
        full_name= f"{first_name} {middle_name} {last_name}"
    else:
        full_name= f"{first_name} {last_name}"
    return full_name.title()
musician= get_formatted_name('jimi', 'hendrix')
print(musician)
musician2= get_formatted_name('john', 'hooker', 'lee')
print(musician2)
