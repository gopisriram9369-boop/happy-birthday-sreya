from flask import Blueprint, render_template
from memories import get_photos

bp = Blueprint("gifts", __name__)

@bp.get("/gifts")
def page():
    return render_template("pages/gifts.html", photos=get_photos(), active="gifts")
