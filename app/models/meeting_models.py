import sqlalchemy
from .. import db

from datetime import datetime

class Meeting( db.Model ):

    id = db.Column( db.Integer, primary_key = True, autoincrement = True )

    uid = db.Column( db.Integer, db.ForeignKey( 'user.id' ), nullable = False )

    tag = db.Column( db.String(200), nullable = False, unique = False )

    date_created = db.Column( db.DateTime, default = datetime.utcnow() )

    members = db.relationship( 'Member', backref = 'meeting', lazy = True )
    polls = db.relationship( 'Poll', backref = 'meeting', lazy = True )

    @staticmethod
    def add( uid:int, tag:str ):
        _meeting = Meeting( uid = uid, tag = tag )

        db.session.add( _meeting )
        db.session.commit()

        return _meeting
    
    @staticmethod
    def edit_tag( meeting_id, tag ):
        _meeting = Meeting.query.get( meeting_id )

        if (_meeting is not None )and (tag is not None):
            _meeting.tag = tag
            db.session.commit()

        return _meeting
    
    @staticmethod
    def pop( meeting_id ):
        _meeting = Meeting.query.get( meeting_id )

        if _meeting is not None:
            _meeting.pop()

        return _meeting

    def pop ( self ):

        for member in self.members:
            member.pop()
        for poll in self.polls:
            poll.pop()

        db.session.delete( self )
        db.session.commit()

        return self