from .. import db

from datetime import datetime

from .vote_models import Vote

class Option( db.Model ):

    id = db.Column( db.Integer, primary_key = True, autoincrement = True )

    pid = db.Column( db.Integer, db.ForeignKey('poll.id') )
    tag = db.Column( db.String(200), nullable = False )
    desc = db.Column( db.String( 500 ), nullable = True )

    votes = db.relationship( 'Vote', backref = "Option", lazy = True )

    @staticmethod
    def add( pid, tag, desc ):
        _option = Option( pid = pid, tag = tag, desc = desc )

        db.session.add( _option )
        db.session.commit()

        return _option
    
    @staticmethod
    def edit( oid, tag = None, desc = None ):
        _option = Option.query.get( oid )

        if _option is not None:

            if tag is not None:
                _option.tag = tag
            
            if desc is not None:
                _option.desc = desc

            db.session.commit()

        return _option
    
    @staticmethod
    def pop_obj( oid ):
        _option = Option.query.get( oid )

        if _option is not None:

            _option.pop()

        return _option

    def pop( self ):

        for vote in self.votes:
            vote.pop()

        db.session.delete( self )

        db.session.commit()

        return self

    def n_votes(self):

        return len(self.votes)