from flask_restful import Resource, reqparse, marshal_with
from flask import abort, Response, request

from ..resources.all_fields import MemberFields
from ..models.member_models import Member

class MemberResource( Resource ):

    c_fields = reqparse.RequestParser()
    c_fields.add_argument( "name", type = str, default = "Anonymouse Member" )
    c_fields.add_argument( "email", type = str, required = True )

    e_fields = reqparse.RequestParser()
    e_fields.add_argument( "email", type = str, required = True )
    e_fields.add_argument( "pwd", type = str, required = True )

    @marshal_with( MemberFields )
    def post( self, meeting_id ):
        # Create a new member in a meeting
        pl = self.c_fields.parse_args( strict = True )

        try:
            return Member.add( meeting_id = meeting_id, **pl )
        except Exception as e:
            abort( Response( str(e), 400 ) )
    
    @marshal_with( MemberFields )
    def put( self, mid = 0, meeting_id = None ):
        # Authenticates member
        if mid == 0:
            abort( 404 )

        pl = self.e_fields.parse_args( strict=True )

        _member = Member.authenticate( mid = mid, **pl )

        if _member is None:
            abort( Response( "Member not found", 404 ) )

        return _member

    @marshal_with( MemberFields )
    def delete( self, mid = 0, meeting_id = None ):
        # deletes a member from a meeting
        if mid == 0:
            abort( 404 )

        try:
            return Member.pop_obj( mid )
        except Exception as e:
            abort( Response( str(e), 400 ) )
