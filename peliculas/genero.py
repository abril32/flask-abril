from . import db
from flask import Blueprint, render_template

bp = Blueprint('genero', __name__,url_prefix="/genero")

@bp.route("/")
def category():
    consulta = """
        SELECT name, category_id FROM category
        ORDER BY name;
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_category = res.fetchall()
    print(lista_category)
    pagina = render_template("genero.html", categorias = lista_category)
    
    return pagina

@bp.route('/<int:id>/detalle')
def detalle(id):
    consulta="""
    SELECT name FROM category
    WHERE category_id = ?
    """
    consulta2 = """
        SELECT f.title as pelicula,c.name as categoria,c.category_id FROM film f
        JOIN film_category fc on f.film_id = fc.film_id
        JOIN category c on fc.category_id = c.category_id 
        WHERE c.category_id = ?
    """
    con = db.get_db()
    res = con.execute(consulta,(id,))
    categoria = res.fetchone()
    res = con.execute(consulta2,(id,))
    lista_peliculas = res.fetchall()
    pagina = render_template("genero-detalle.html", peliculas=lista_peliculas, categoria=categoria)
    
    return pagina