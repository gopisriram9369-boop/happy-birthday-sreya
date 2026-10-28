from flask import Blueprint, render_template
from memories import get_photos

bp = Blueprint("letter", __name__)

@bp.get("/letter")
def page():
    return render_template("pages/letter.html", photos=get_photos(), active="letter")
