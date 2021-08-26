from .. import app
from ..models.meeting_models import Meeting
from flask import render_template, redirect, url_for, session

def val_active_session():

    if ( session.get( 'data' ) is None ):
        return redirect( url_for( "login_view" ) )


@app.route("/")
def index():

    if ( session.get( 'data' ) is None ):
        return redirect( url_for( "login_view" ) )

    meetings = Meeting.query.filter_by( 
        uid = session['data']['id'] 
    ).order_by( Meeting.id.desc() ).all()

    print( meetings, session['data']['id'] )

    return render_template( "base.html", meetings = meetings )

@app.route( "/meeting/<int:meeting_id>/polls" )
def meeting_polls_view( meeting_id:int ):

    if ( session.get( 'data' ) is None ):
        return redirect( url_for( "login_view" ) )

    return render_template( 
        "meeting_polls.html", 
        meeting = Meeting.query.get( meeting_id )
    )

@app.route( "/logout" )
def logout_view():

    if ( session.get( 'data' ) is None ):
        return redirect( url_for( "login_view" ) )

    session.pop("data")

    return redirect( url_for( "index" ) )