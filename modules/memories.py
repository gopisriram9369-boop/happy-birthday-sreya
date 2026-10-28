from flask import Blueprint, render_template
from memories import get_photos

bp = Blueprint("memories", __name__)

@bp.get("/memories")
def page():
    return render_template("pages/memories.html", photos=get_photos(), active="memories")
