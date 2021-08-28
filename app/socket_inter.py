from . import socket

from flask_socketio import send, emit, join_room, leave_room, rooms


@socket.on( "connect" )
def socket_connect():

    send( "socket connected" )

# TODO: on join room, on leave room (room is the meeting ID)
