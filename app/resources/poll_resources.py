from flask_restful import Resource, reqparse, marshal_with
from flask import abort, Response, request

from ..resources.all_fields import PollFields
from ..models.poll_models import Poll

class PollResource( Resource ):

    c_fields = reqparse.RequestParser()
    c_fields.add_argument( "tag", type = str, required = True )
    c_fields.add_argument( "desc", type = str, required = False )

    e_fields = reqparse.RequestParser()
    e_fields.add_argument( "tag", type = str, required = False )
    e_fields.add_argument( "desc", type = str, required = False )

    @marshal_with( PollFields )
    def post( self, meeting_id = 0, pid = 0 ):
        # Create a new poll
        if meeting_id == 0:
            abort(404)
        pl = self.c_fields.parse_args( strict = True )

        try:
            return Poll.add( meeting_id = meeting_id, **pl )
        except Exception as e:
            abort( Response( str(e), 400 ) )

    @marshal_with( PollFields )
    def put( self, pid = 0, meeting_id = 0 ):
        # Edits a poll
        if ( pid == 0 ):
            abort(404)

        pl = self.e_fields.parse_args( strict = True )

        try:
            return Poll.edit( pid = pid, **pl )
        except Exception as e:
            abort( Response( str(e), 400 ) )

    @marshal_with( PollFields )
    def delete( self, pid = 0, meeting_id = 0 ):
        # deletes a poll
        if pid == 0:
            abort( 404 )
        try:
            return Poll.pop( pid )
        except Exception as e:
            abort( Response( str(e), 400 ) )
