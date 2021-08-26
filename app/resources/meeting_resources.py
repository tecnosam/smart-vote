from flask_restful import Resource, reqparse, marshal_with
from flask import abort, Response, request

from ..resources.all_fields import MeetingFields
from ..models.meeting_models import Meeting

class MeetingResource( Resource ):

    c_fields = reqparse.RequestParser()
    c_fields.add_argument( "uid", type = str, required = True )
    c_fields.add_argument( "tag", type = str, required = True )

    e_fields = reqparse.RequestParser()
    e_fields.add_argument( "tag", type = str, required = False )

    @marshal_with( MeetingFields )
    def get( self, uid = 0,meeting_id = 0 ):

        if uid == 0:
            abort( 404 )

        return Meeting.query.filter_by( 
            uid = uid
        ).all() if meeting_id is 0 else Meeting.query.get( meeting_id )

    @marshal_with( MeetingFields )
    def post( self, uid = 0, meeting_id = 0 ):
        # Create a new meeting
        if uid is 0:
            abort( 404 )

        tag = request.args.get( 'tag', "New Meeting form" )

        try:
            return Meeting.add( uid = uid, tag = tag )
        except Exception as e:
            abort( Response( str(e), 500 ) )

    @marshal_with( MeetingFields )
    def put( self, meeting_id = 0, uid = 0 ):
        # Edits a meeting
        # pl = self.e_fields.parse_args( strict = True )
        if meeting_id == 0:
            abort(404)

        tag = request.args['tag']

        try:
            return Meeting.edit_tag( meeting_id, tag )
        except Exception as e:
            abort( Response( str(e), 400 ) )

    @marshal_with( MeetingFields )
    def delete( self, meeting_id = 0, uid = 0 ):
        # deletes a meeting

        if meeting_id == 0:
            abort( 404 )

        try:
            return Meeting.pop_obj( meeting_id )
        except Exception as e:
            abort( Response( str(e), 400 ) )
