from auth.decorators import requires_auth
from flask import Blueprint, redirect, render_template, session, url_for


webapp_bp = Blueprint('webapp', __name__, template_folder="templates")


@webapp_bp.route("/")
def home():
    """
    Home endpoint
    """

    return render_template("home.html")


@webapp_bp.route("/profile")
@requires_auth
def profile():
    """
    Protected endpoint which displays your profile if you are logged in, otherwise it prompts the user to log in
    """
    return render_template(
        'profile.html',
        session=session.get('user')
    )



@webapp_bp.route("/redirect-example")
def redirect_example():

    return redirect(url_for("webapp.home"))


@webapp_bp.route("clear-session-example")
def session_clearing():
    session.clear()
    return redirect(url_for("webapp.home"))
