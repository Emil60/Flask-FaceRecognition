from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class imageForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(), Length(min=2, max=50)])
    photo = FileField()
    submit = SubmitField('Check')