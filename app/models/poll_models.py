from .. import db

from datetime import datetime

class Poll( db.Model ):

    id = db.Column( db.Integer, primary_key = True, autoincrement = True )
    meeting_id = db.Column( db.Integer, db.ForeignKey('meeting.id') )
    tag = db.Column( db.String(200), nullable = False )
    desc = db.Column( db.String( 500 ), nullable = True )

    options = db.relationship( 'Option', backref = "poll", lazy = True )

    @staticmethod
    def add( meeting_id:int, tag:str, desc:str = None ):

        _poll = Poll( meeting_id = meeting_id, tag = tag, desc = desc )

        db.session.add( _poll )
        db.session.commit()

        return _poll

    @staticmethod
    def edit( pid, tag = None, desc = None ):
        _poll = Poll.query.get( pid )

        if _poll is not None:

            if tag is not None:
                _poll.tag = tag

            if desc is not None:
                _poll.desc = desc

            db.session.commit()
        return _poll
    
    @staticmethod
    def pop_obj( pid ):
        _poll = Poll.query.get( pid )

        if _poll is not None:
            _poll.pop()

        return _poll

    def pop( self ):

        for option in self.options:
            option.pop(  )

        db.session.delete( self )
        db.session.commit()

        return self