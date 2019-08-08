from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class CreateStoreForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired()])
    image = FileField('Image')
    submit = SubmitField('Save')
