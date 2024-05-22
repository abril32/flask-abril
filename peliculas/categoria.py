from . import db
from flask import Blueprint, render_template

bp = Blueprint('categoria', __name__,url_prefix="/categoria")

@bp.route("/")
def category():
    consulta = """
        SELECT name FROM category
        ORDER BY name;
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_category = res.fetchall()
    pagina = render_template("category.html", categorias = lista_category)
    
    return pagina

@bp.route('/<int:id>/detalle')
def detalle():
    consulta = """
        SELECT f.title as pelicula,c.name as categoria,c.category_id FROM film f
        JOIN film_category fc on f.film_id = fc.film_id
        JOIN category c on fc.category_id = c.category_id 
        WHERE c.category_id = ?
        GROUP BY c.category_id
    """
    con = db.get_db()
    res = con.execute(consulta,(id))
    categoria= {"nombre": res["categoria"], "id": res["c.category_id"]}
    categoria = res["categoria"]
    lista_category = res.fetchall()
    pagina = render_template("category.html", categorias = lista_category)
    
    return pagina