from .. import db
from cryptography.fernet import Fernet

class Member( db.Model ):

    id = db.Column( db.Integer, primary_key = True, autoincrement = True )

    meeting_id = db.Column( db.Integer, db.ForeignKey('meeting.id') )

    name = db.Column( db.String( 200 ), nullable = False, unique = False )
    email = db.Column( db.String( 200 ), nullable = False, unique = False )

    pwd = db.Column( db.String( 400 ), nullable = False, unique = False )

    votes = db.relationship( 'Vote', backref = 'member', lazy = True )

    @staticmethod
    def add( meeting_id, name, email ):
        _member = Member(
            meeting_id = meeting_id, 
            email = email,
            name = name,
            pwd = Fernet.generate_key().decode()[:8]
        )

        db.session.add( _member )
        db.session.commit()

        return _member
    
    @staticmethod
    def authenticate( meeting_id, email, pwd ):

        return Member.query.filter_by(
            meeting_id = meeting_id,
            email = email,
            pwd = pwd
        ).first()

    @staticmethod
    def pop_obj( mid ):
        _member = Member.query.get( mid )

        if _member is not None:
            _member.pop(  )

        return _member

    def pop(self):

        print( self )

        for vote in self.votes:
            vote.pop()

        db.session.delete( self )
        db.session.commit()

        return self
