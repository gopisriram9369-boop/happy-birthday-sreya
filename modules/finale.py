from flask import Blueprint, render_template
from memories import get_photos

bp = Blueprint("finale", __name__)

@bp.get("/finale")
def page():
    return render_template("pages/finale.html", photos=get_photos(), active="finale")
