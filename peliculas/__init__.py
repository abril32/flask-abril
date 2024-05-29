from flask import Flask

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)
    

@app.route('/')
def hello():
    return 'Hello, World!'

from . import lenguajes
app.register_blueprint(lenguajes.bp)


from . import genero
app.register_blueprint(genero.bp)