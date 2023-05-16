##############################################
#                                            #
#     Copyright, this script is owned by     #
#        MoneySmart Investment Group         #
#                                            #
#                                            #
#      M   M     SSS     IIIII     GGG       #
#      MM MM    S   S      I      G   G      #
#      MM MM    S          I      G          #
#      M M M     SSS       I      GGGGG      #
#      M   M        S      I      G   G      #
#      M   M    S   S      I      G   G      #
#      M   M     SSS     IIIII     GGG       #
#                                            #
#                                            #
#             All right reserved             #
# https://www.moneysmartinvestmentgroup.com  #
#                                            #
##############################################

### import external module and var ###
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

### create var to use in the app ###
db = SQLAlchemy()
app = Flask(__name__)
#def create_app(config_filename):
#    app.config.from_pyfile('config.py')
#    db.init_app(app)
#    with app.app_context(): 
#        db.create_all()

#    return app
    
### to avoid cycling import, import external module here ###
from project import database, route