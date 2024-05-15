from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route("/lenguaje")
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

@app.route("/category")
def category():
    consulta = """
        SELECT name FROM category
        ORDER BY name;
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_category = res.fetchall()
    pagina = render_template("category.html", categoria = lista_category)
    
    return pagina