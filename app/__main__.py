from . import socket, app

if __name__ == '__main__':
    socket.run( app, port = 5000, debug = True )
    # app.run( debug = True )