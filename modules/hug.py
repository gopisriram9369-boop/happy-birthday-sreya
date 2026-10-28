from flask import Blueprint, render_template
from memories import get_photos

bp = Blueprint("hug", __name__)

@bp.get("/hug")
def page():
    return render_template("pages/hug.html", photos=get_photos(), active="hug")
