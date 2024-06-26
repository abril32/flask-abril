from . import db
from flask import Blueprint, render_template

bp = Blueprint('actor', __name__,url_prefix="/actor")

@bp.route("/")
def actor():
    consulta = """
        SELECT first_name, last_name, actor_id FROM actor
        ORDER by last_name;
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_actores = res.fetchall()
    print(lista_actores)
    pagina = render_template("actor.html", actores = lista_actores)
    
    return pagina

@bp.route('/<int:id>/detalle')
def detalle(id):
    consulta="""
       SELECT first_name, last_name FROM actor
       WHERE actor_id = ?
    """
    consulta2 = """
        SELECT f.title as pelicula, f.film_id, fa.actor_id FROM film_actor fa
        JOIN film f on fa.film_id = f.film_id
        WHERE fa.actor_id = ?
    """
    con = db.get_db()
    res = con.execute(consulta,(id,))
    actor = res.fetchone()
    res = con.execute(consulta2,(id,))
    lista_peliculas = res.fetchall()
    pagina = render_template("actor-detalle.html", pelis=lista_peliculas, actor=actor)
    
    return pagina