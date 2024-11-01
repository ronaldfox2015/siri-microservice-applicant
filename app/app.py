import logging
from flask import Flask, jsonify

from app.interface.applicant_controller import applicant_controller
from app.interface.apply_controller import apply_controller
from app.interface.notification_controller import notification_controller
from app.interface.user_controller import user_controller
from app.applicant.infrastructure.db.models import db
from app.interface.home_controller import post_health
from app.interface.announcement_controller import announcement_controller
from app.interface.applicant_documents_controller import applicant_documents_controller

import os


app = Flask(__name__, template_folder='/app/notification/infrastructure/templates/')
mysql = f'mysql+pymysql://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@{os.getenv("MYSQL_HOST")}:3306/{os.getenv("MYSQL_DATABASE")}'
# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = mysql
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Configurar el logging
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)  # Nivel de logging


# Inicializar la base de datos
db.init_app(app)
# Inicializar la base de datos
app.register_blueprint(post_health, url_prefix='/v1/applicant')
app.register_blueprint(user_controller, url_prefix='/v1/user')
app.register_blueprint(applicant_controller, url_prefix='/v1/applicant')
app.register_blueprint(apply_controller, url_prefix='/v1/applicant')

app.register_blueprint(notification_controller, url_prefix='/v1/notification')

app.register_blueprint(announcement_controller, url_prefix='/v1/announcement')
app.register_blueprint(applicant_documents_controller, url_prefix='/v1/applicant_documents')
# @app.errorhandler(Exception)
# def handle_exception(e):
#     """Manejar excepciones globalmente."""
#     response = {
#         "code": 400,
#         "message": str(e),
#         "data": {}
#     }
#     app.logger.info(e)
#     if isinstance(e, KeyError):
#         response["code"] = 400*10
#         return jsonify(response), 400
#     elif isinstance(e, ZeroDivisionError):
#         response["code"] = 400*10
#         return jsonify(response), 400
#     elif isinstance(e, Exception):
#         response["code"] = 400*10
#         return jsonify(response), 400
#     return jsonify(response), 500

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'resources', 'aplicant_documents')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
