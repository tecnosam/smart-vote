from flask_restful import Resource, reqparse, marshal_with
from flask import abort, Response, request

from ..resources.all_fields import UserFields
from ..models.user_models import User

class UserResource( Resource ):

    c_fields = reqparse.RequestParser()
    c_fields.add_argument( "name", type = str, default = "New User" )
    c_fields.add_argument( "email", type = str, required = True )
    c_fields.add_argument( "pwd", type = str, required = True )

    e_fields = reqparse.RequestParser()
    e_fields.add_argument( "name", type = str, required = False )
    e_fields.add_argument( "email", type = str, required = False )
    e_fields.add_argument( "pwd", type = str, required = False )

    @marshal_with( UserFields )
    def post( self, uid = 0 ):
        # Create a new user
        pl = self.c_fields.parse_args( strict = True )

        try:
            _user =  User.add( **pl )
        except Exception as e:
            abort( Response(str(e), 400) )

        if _user is None:
            print( "foo", _user )
            abort( Response( "Invalid Email or password", 400 ) )

        print("bar")

        return _user

    @marshal_with( UserFields )
    def put( self, uid = None ):
        # Edits a user
        if uid is None:
            abort( 400 )

        pl = self.e_fields.parse_args( strict = True )

        _user = User.edit( uid = uid, **pl )
        if _user is None:

            abort( Response( "User not found", 404 ) )

        return _user

    @marshal_with( UserFields )
    def delete( self, uid = None ):
        # deletes a user
        if uid is None:
            abort(404)

        _user = User.pop( uid )
        if _user is None:

            abort( Response( "User not found", 404 ) )

        return _user