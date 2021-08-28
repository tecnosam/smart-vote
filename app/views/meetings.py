from app.models.vote_models import Vote
from app.models.meeting_models import Meeting
from ..models.member_models import Member
from .. import app

from flask import redirect, request, url_for, render_template, session, abort

from werkzeug.utils import secure_filename

import sys, os
import json, csv

@app.route( "/meetings/<int:meeting_id>/members/import", methods = ['POST'] )
def import_members( meeting_id:int ):
    file = request.files[ 'members' ]

    fn = os.path.join( "tmp", secure_filename( file.filename ) )

    file.save( fn )

    with open( fn, "r" ) as f:
        try:
            data = json.load( f )
            for member in data:
                try:
                    Member.add( meeting_id=meeting_id, name=member['name'], email = member['email'] )
                except:
                    pass
        except json.JSONDecodeError:
            pass

    return redirect( url_for( 'index' ) )

@app.route( "/vote/<int:meeting_id>" )
def vote_view( meeting_id:int ):

    meeting = Meeting.query.get( meeting_id )

    if meeting is None:
        abort( 404 )
    
    if ( session.get("member") is None ):
        return render_template(
            "member_login.html", 
            meeting = meeting,
            meeting_id = meeting_id
        )
    
    elif ( session['member']['meeting_id'] != meeting_id ):

        session.pop( "member" )

        return redirect( url_for("vote_view", meeting_id = meeting_id) )
    
    val_submitted = Vote.query.filter_by( mid = session['member']['id'] ).first()

    if val_submitted is not None:
        return redirect( url_for( "vote_results_view", meeting_id = meeting_id ) )


    return render_template(
        "vote.html", 
        meeting = meeting, 
        meeting_id = meeting_id
    )

@app.route("/result/<meeting_id>")
def vote_results_view( meeting_id ):
    return "WIP"
    return render_template("")
