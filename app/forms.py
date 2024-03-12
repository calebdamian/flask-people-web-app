from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class PersonaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message="Por favor ingresa tu nombre"), Length(min=2, max=50)])
    apellido = StringField('Apellido', validators=[DataRequired(message="Por favor ingresa tu apellido"), Length(min=2, max=50)])
    edad = IntegerField('Edad', validators=[DataRequired(message="Por favor ingresa tu edad"), NumberRange(min=0, max=150)])
    direccion = StringField('Dirección', validators=[Length(max=100)])
    correo = StringField('Correo', validators=[DataRequired(message="Por favor ingresa tu correo electrónico"), Email()])
    submit = SubmitField('Añadir nueva persona')
    