from flask_restful import fields

# TODO: Add all resources to api


VoteFields = {
    "id": fields.Integer,
    "mid": fields.Integer, # mid is member id
    "oid": fields.Integer, # oid is option id
}

OptionFields = {
    "id": fields.Integer,
    "pid": fields.Integer,
    "tag": fields.String,
    "desc": fields.String,
    "votes": fields.Nested( VoteFields ),
}

PollFields = {
    "id": fields.Integer,
    "meeting_id": fields.Integer,
    "tag": fields.String,
    "options": fields.Nested( OptionFields ),
    "desc": fields.String,
}

MemberFields = {
    "id": fields.Integer,
    "meeting_id": fields.Integer,
    "name": fields.String, 
    "email": fields.String, 
    "pwd": fields.String, 
    "votes": fields.Nested(VoteFields), 
}

MeetingFields = {
    "id": fields.Integer,
    "uid": fields.Integer,
    "tag": fields.String,
    "polls": fields.Nested( PollFields ),
    "members": fields.Nested( MemberFields ),
    "date_created": fields.DateTime,
}

UserFields = {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
    "pwd": fields.String,
    "meetings": fields.Nested( MeetingFields ),
    "date_created": fields.DateTime,
}