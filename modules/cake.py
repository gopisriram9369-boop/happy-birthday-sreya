from flask import Blueprint, render_template
from memories import get_photos

bp = Blueprint("cake", __name__)

@bp.get("/cake")
def page():
    return render_template("pages/cake.html", photos=get_photos(), active="cake")
