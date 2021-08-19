from flask_restful import Resource, reqparse, marshal_with
from flask import abort, Response, request

from ..resources.all_fields import VoteFields

from ..models.vote_models import Vote
from ..models.member_models import Member
from ..models.option_models import Option

class VoteResource( Resource ):

    c_fields = reqparse.RequestParser()
    c_fields.add_argument( "mid", type = int, required = True )
    c_fields.add_argument( "oid", type = int, required = True )

    @marshal_with( VoteFields )
    def post( self, mid, oid, vid = 0 ):
        # Create a new vote
        # pl = self.c_fields.parse_args( strict = True )

        # TODO: validate the members username and password in header
        _vote = Vote.query.filter_by( mid = mid, oid = oid ).first()

        if _vote is not None:
            abort( Response( "You cannot vote twice", 403 ) )

        if Member.query.get( mid ) is None:
            abort( Response("Member does not exist", 404) )

        if Option.query.get( oid ) is None:
            abort( Response("Option does not exist", 404) )

        try:
            return Vote.add( mid, oid )
        except Exception as e:
            abort( Response( str(e), 400 ) )