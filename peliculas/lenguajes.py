from . import db
from flask import Blueprint, render_template

bp = Blueprint('idioma', __name__,url_prefix="/idioma")

@bp.route("/")
def lenguaje():
    consulta = """
        SELECT name FROM language
        ORDER BY name;
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_lenguaje = res.fetchall()
    pagina = render_template("language.html",
                             lenguajes = lista_lenguaje)

    return pagina

