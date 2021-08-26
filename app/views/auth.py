from flask.templating import render_template
from .. import app

from ..models.user_models import User
from ..resources.all_fields import UserFields

from flask import session, request, jsonify, flash, redirect, url_for

from flask_restful import marshal

@app.route("/login", methods = ['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['pwd']

        _user = User.auth( email, pwd )

        if _user is None:
            flash("Invalid login details, please try again", "error")

        else:
            _user.pwd = pwd
            session[ 'data' ] = marshal( _user, UserFields )

            session['immutable'] = [ 'meetings', 'date_created', 'id' ]

            return redirect( url_for("index") )

    return render_template( "login.html" )


@app.route("/signup", methods = ['GET', 'POST'])
def signup_view():

    return render_template( "signup.html" )