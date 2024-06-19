from . import db
from flask import Blueprint, render_template

bp = Blueprint('peliculas', __name__,url_prefix="/peliculas")

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
        SELECT title FROM film
        WHERE film_id = ?
    """
    consulta2 = """
        SELECT  FROM 
        JOIN  on  = 
        JOIN  on  = 
        WHERE = ?
    """
    con = db.get_db()
    res = con.execute(consulta,(id,))
    peliculas = res.fetchone()
    res = con.execute(consulta2,(id,))
    lista_peliculas = res.fetchall()
    pagina = render_template("peli-detalle.html", peliculas=lista_peliculas, pelicula=peliculas)
    
    return pagina