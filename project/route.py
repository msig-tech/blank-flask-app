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
from flask import render_template
from project.factory import app

### english ###
@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def english():
    
    return render_template('en/home.html', title="Welcome")

### francais ###
@app.route("/francais", methods=['GET', 'POST'])
def francais():
    
    return render_template('fr/home.html', title="Bienvenue")