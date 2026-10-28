from flask import Blueprint, render_template
from memories import get_photos
bp = Blueprint("paris", __name__)
@bp.get("/paris")
def page():
    return render_template("pages/paris.html", photos=get_photos(), active="paris")
