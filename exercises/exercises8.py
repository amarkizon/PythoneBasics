# 8-9. Magicians:
def show_magicians(names):  # Looping magician names
    for name in names:
        print(f"Please welcome magician, {name.title()} !!!")

magicians = ['david', 'raja', 'john']   # Listing magician names
show_magicians(magicians)

# 8-10. Great Magicians:

def make_great(names: list):
    great_name = []
    for name in names:
        great_name.append(f"the Great {name}")
    return great_name
magicians = make_great(magicians)
make_great(magicians)
show_magicians(magicians)
