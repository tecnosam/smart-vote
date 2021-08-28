from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

import os

from dotenv import load_dotenv

load_dotenv()

app = Flask( __name__ )

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv( "DB_URI" )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.secret_key = os.getenv( "FLASK_SECRET_KEy" )

db = SQLAlchemy( app )

from .models.user_models import *
from .models.meeting_models import *
from .models.member_models import *
from .models.option_models import *
from .models.poll_models import *
from .models.vote_models import *

db.create_all()

socket = SocketIO( app )

from .socket_inter import *

api = Api( app )

from .resources.meeting_resources import MeetingResource
from .resources.member_resources import MemberResource
from .resources.option_resources import OptionResource
from .resources.poll_resources import PollResource
from .resources.user_resources import UserResource
from .resources.vote_resources import VoteResource

api.add_resource( UserResource, "/users", "/users/<int:uid>" )

api.add_resource( MeetingResource, "/users/<int:uid>/meetings", "/meetings/<int:meeting_id>" )

api.add_resource( MemberResource, "/meetings/<int:meeting_id>/members", "/meetings/members/<int:mid>" )

api.add_resource( PollResource, "/meetings/<int:meeting_id>/polls", "/meetings/polls/<int:pid>" )

api.add_resource( OptionResource, "/polls/<int:pid>/options", "/polls/options/<int:oid>" )

api.add_resource( VoteResource, "/meetings/members/<int:mid>/vote/<int:oid>" )

api.init_app( app )

from .views.views import *
from .views.auth import *
from .views.meetings import *

# TODO> activate, deactivate form feature

# TODO: socket io interactions for realtime voting results
