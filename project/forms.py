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
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, validators
from wtforms.validators import DataRequired

 
class RegistrationForm(FlaskForm):
    langage = HiddenField('Language')
    firstname = StringField('FirstName', validators=[DataRequired()])
    lastname = StringField('LastName', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), validators.Email(message="Please, enter a valid email address, example : example@domain.com")])
    submit = SubmitField(f"Your informations are correctly sent, thanks!") 


class DeleteMemberForm(FlaskForm):
    submit = SubmitField('Unsubscribe', validators=[DataRequired()])