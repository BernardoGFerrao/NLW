from flask import Flask
from flask_cors import CORS
from RocketSeat.NLW.src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

#Criação de rotas
from RocketSeat.NLW.src.main.routes.event_routes import event_route_bp
app.register_blueprint(event_route_bp)