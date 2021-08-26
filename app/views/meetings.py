
from ..models.member_models import Member
from .. import app

from flask import redirect, request, url_for

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