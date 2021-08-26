from flask_restful import Resource, reqparse, marshal_with
from flask import abort, Response, request

from ..resources.all_fields import OptionFields

from ..models.option_models import Option
class OptionResource( Resource ):

    c_fields = reqparse.RequestParser()
    c_fields.add_argument( "tag", type = str, required = True )
    c_fields.add_argument( "desc", type = str, required = False )

    e_fields = reqparse.RequestParser()
    e_fields.add_argument( "tag", type = str, required = False )
    e_fields.add_argument( "desc", type = str, required = False )

    @marshal_with( OptionFields )
    def post( self, pid:int = 0, oid = 0 ):
        # Create a new option in poll

        if pid == 0:
            abort(404)

        pl = self.c_fields.parse_args( strict = True )

        try:
            return Option.add( pid = pid, **pl )
        except Exception as e:
            abort( Response( str(e), 400 ) )

    @marshal_with( OptionFields )
    def put( self, oid = 0, pid = 0 ):
        # Edits a option in poll
        if oid == 0:
            abort(404)
        pl = self.e_fields.parse_args( strict = True )

        try:
            return Option.edit( oid = oid, **pl )
        except Exception as e:
            abort( Response( str(e), 400 ) )

    @marshal_with( OptionFields )
    def delete( self, oid = 0, pid = 0 ):
        # deletes a option in poll

        if oid == 0:
            abort(404)

        try:
            return Option.pop_obj( oid )
        except Exception as e:
            abort( Response( str(e), 400 ) )
