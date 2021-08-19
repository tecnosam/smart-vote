from .. import db

class Vote( db.Model ):

    id = db.Column( db.Integer, primary_key = True, autoincrement = True )

    mid = db.Column( db.Integer, db.ForeignKey( 'member.id' ) )
    oid = db.Column( db.Integer, db.ForeignKey( 'option.id' ) )

    @staticmethod
    def add( mid, oid ):
        _vote = Vote( mid = mid, oid = oid )

        db.session.add( _vote )
        db.session.commit(  )

        return _vote

    def pop( self ):

        db.session.delete( self )
        db.session.commit()

        return self

# VOTES CAN ONLY BE ADDED, CANNOT BE DELETED OR MODIFIED FROM THE API