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
from project.factory import app
from project.stuff import secret_key, db_username, db_password, db_domain, db_name, mail_server, mail_port, mail_username, mail_password

### MySQL connexion ###
app.config['SECRET_KEY'] = secret_key
#app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_username}:{db_password}@{db_domain}/{db_name}"

### email configuration ###
app.config['MAIL_SERVER']= mail_server
app.config['MAIL_PORT'] = mail_port
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

### you can use this for revert module to get the correct url (put domain on "server_name" var on stuff.py) ###
#app.config['SERVER_NAME'] = 'server_name'

