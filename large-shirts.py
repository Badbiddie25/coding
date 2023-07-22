# -4. Large Shirts: Modify the make_shirt() function so that shirts are large 
# by default with a message that reads I love Python. Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a different 
# message.

def make_shirt(size="large",moto='I love python'):
    sizes=['small', 'medium']
    if size in sizes:
        print("This is your option:" + moto.title())
    else:
        print("Sorry, we don't have that option in your size")

make_shirt(size='large')
make_shirt(size='medium')
make_shirt(size='small', moto='you suck')