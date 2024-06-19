from . import db
from flask import Blueprint, render_template

bp = Blueprint('peli', __name__,url_prefix="/peli")

@bp.route("/")
def peli():
    consulta = """
        SELECT title, film_id FROM film
        ORDER by title ASC
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_peliculas = res.fetchall()
    print(lista_peliculas)
    pagina = render_template("peli.html", pelis = lista_peliculas)
    
    return pagina

@bp.route('/<int:id>/detalle')
def detalle(id):
    consulta="""
        SELECT title,description,length,rating,release_year FROM film
        WHERE film_id = ?
    """
    consulta2 = """
        SELECT first_name,last_name, a.actor_id FROM film_actor fa
        JOIN actor a on fa.actor_id = a.actor_id
        WHERE film_id = ?
    """
    con = db.get_db()
    res = con.execute(consulta,(id,))
    pelicula = res.fetchone()
    res = con.execute(consulta2,(id,))
    lista_actores = res.fetchall()
    pagina = render_template("peli-detalle.html", actores=lista_actores, pelicula=pelicula)
    
    return pagina