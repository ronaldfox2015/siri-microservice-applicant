import os
from flask import Flask, jsonify
from app.applicant.infrastructure.db.models import db
from app.interface.home_controller import post_health

app = Flask(__name__)


# Manejador de error 404 - Página no encontrada
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="404 Not Found", message="The requested URL was not found on the server."), 404


# Configuración de la base de datos
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@{os.getenv("MYSQL_HOST")}/{os.getenv("MYSQL_DATABASE")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Inicializar la base de datos
app.register_blueprint(post_health, url_prefix='/v1/applicant')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
