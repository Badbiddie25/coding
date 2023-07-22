def make_shirt(size,moto):
    sizes=['small', 'medium']
    if size in sizes:
        print("This is your option:" + moto.title())
    else:
        print("Sorry, we don't have that option in your size")

make_shirt(size='small',moto='You suck')