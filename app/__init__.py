from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

import os

from dotenv import load_dotenv

load_dotenv()

app = Flask( __name__ )

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv( "DB_URI" )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy( app )

from .models.user_models import *
from .models.meeting_models import *
from .models.member_models import *
from .models.option_models import *
from .models.poll_models import *
from .models.vote_models import *

db.create_all()

api = Api( app )

from .resources.meeting_resources import MeetingResource
from .resources.member_resources import MemberResource
from .resources.option_resources import OptionResource
from .resources.poll_resources import PollResource
from .resources.user_resources import UserResource
from .resources.vote_resources import VoteResource

api.add_resource( UserResource, "/auth", "/auth/<int:uid>" )

api.add_resource( MeetingResource, "/user/<int:uid>/meetings", "/meetings/<int:meeting_id>" )

api.add_resource( MemberResource, "/meetings/<int:meeting_id>/members", "/meeting/members/<int:mid>" )

api.add_resource( PollResource, "/meetings/<int:meeting_id>/polls", "/meeting/polls/<int:pid>" )

api.add_resource( OptionResource, "/polls/<int:pid>/options", "/poll/options/<int:oid>" )

api.add_resource( VoteResource, "/meeting/members/<int:mid>/vote/<int:oid>" )

api.init_app( app )

# TODO: Start work on the frontend