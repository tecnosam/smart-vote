from . import socket

from flask_socketio import send, emit, join_room, leave_room, rooms


@socket.on( "connect" )
def socket_connect():

    send( "socket connected" )

@socket.on('join')
def on_join(data):
    room = f"meeting-{data['meeting_id']}-room"

    join_room(room)

    send('has entered the room.', room=room)

@socket.on('leave')
def on_leave(data):
    room = data['room']

    leave_room(room)

    send('has left the room.', room=room)