from flask import Blueprint, render_template
from memories import get_photos

bp = Blueprint("home", __name__)

@bp.get("/")
def page():
    return render_template("pages/home.html", photos=get_photos(), active="home")
