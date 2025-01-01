# override enter and exit

class Manager(object):
    def __enter__(self):
        print( 'Entering')
        return 'some value'

    def __exit__(self, ty, val, tb):
        #ty, val, tb are for excetions
        print('Exiting')
        print(ty, val, tb)