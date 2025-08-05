from flask import Flask

# importando o sqlalchmey e o migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
#  Diz ao SQLALchemy qual banco usar e como se conectar
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

#  Desativa um recurso que rastreia modificações nos objetos para enconomizar memória
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# diz ao sql qual o app que ele vai usar
db = SQLAlchemy(app)

# conecta o migrate no app e no banco
migrate = Migrate(app, db)

from app.views import homepage
from app.models import Contato
