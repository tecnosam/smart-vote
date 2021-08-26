import sqlalchemy
from .. import db

from datetime import datetime
from hashlib import sha256

class User( db.Model ):

    id = db.Column( db.Integer, primary_key = True, autoincrement = True )

    name = db.Column( db.String(100), nullable = False )
    email = db.Column( db.String( 200 ), unique = True )
    pwd = db.Column( db.String( 300 ), nullable = False )

    date_created = db.Column( db.DateTime, default = datetime.utcnow() )

    meetings = db.relationship( 'Meeting', backref = "user", lazy = True )

    @staticmethod
    def add( name:str, email:str, pwd:str ):
        # The add function checks if user exists, if exists, tries to auth else creates user
        h_pwd = sha256( pwd.encode() ).hexdigest()

        _user = User.query.filter_by( email = email ).first()

        if _user is not None:
            raise Exception( "User with email {} exists!!!!".format( email ) )

        _user = User(
            name = name, email = email, pwd = h_pwd
        )

        try:

            db.session.add( _user )
            db.session.commit()

        except sqlalchemy.exc.IntegrityError:

            db.session.rollback()
            raise Exception( "User with email {} exists!!!!".format( email ) )
        
        except Exception as e:
            db.session.rollback()
            raise e

        return _user
    
    @staticmethod
    def auth( email, pwd ):
        return User.query.filter_by( email = email, pwd = pwd ).first()

    @staticmethod
    def edit( uid:int, name:str = None, email:str = None, pwd:str = None ):
        _user = User.query.get( uid )

        if _user is not None:

            if name is not None:
                _user.name = name

            if email is not None:
                _user.email = email

            if pwd is not None:
                _user.pwd = sha256( pwd.encode() ).hexdigest()

            db.session.commit()

        return _user

    @staticmethod
    def pop( uid:int ):
        _user = User.query.get( uid )

        if _user is not None:

            for meeting in _user.meetings:
                meeting.pop()

            db.session.delete()
            db.session.commit()


        return _user

    @staticmethod
    def auth( email:str, pwd:str ):
        
        return User.query.filter_by( 
            email = email,
            pwd = sha256( pwd.encode() ).hexdigest()
        ).first()