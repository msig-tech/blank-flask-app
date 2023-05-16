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
from project.factory import db
from sqlalchemy import Column, String, DateTime, Boolean
from datetime import datetime
import base64, os

### create your database table here   ###
class User(db.Model):
    # (with 33 random characters for id (more than 1 Decillion (1^60) possibility)) (exact number : 1,176,683,590,872,606,658,877,372,438,191,160,041,869,200,847,992,074,374,682,431,212,028,520,228,618,010,291,694,423,968,321,219,256,949,776,593,274,257,606,372,582,570,993,457,659,214,404,984,560,794,933,646,734,112,532,014,270,395,704,554,763,380,150,692,053,534,551,209,041,272,000,000,000,000,000,000,000,000,000,000,000,000)
    id = Column(String(34), primary_key=True, unique=True, default=lambda: base64.urlsafe_b64encode(os.urandom(33)).rstrip(b'=').decode())
    langage = Column(String(64))
    firstname = Column(String(128))
    lastname = Column(String(128))
    email = Column(String(128), nullable=False)
    # take the datetimenow (server side) as the register var
    register = Column(DateTime, nullable=False, default=datetime.utcnow)
