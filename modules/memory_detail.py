from flask import Blueprint, render_template, abort
from memories import get_photos

bp = Blueprint("memory_detail", __name__)

@bp.get("/memories/<int:photo_id>")
def detail(photo_id):
    photos = get_photos()
    if photo_id < 1 or photo_id > len(photos):
        abort(404)
    return render_template("pages/photo_detail.html", photo=photos[photo_id - 1], photos=photos, active="memories")
