from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired, Length


class MessageForm(FlaskForm):
    title = TextField('Title', validators=[DataRequired()])
    description = TextField('Description',
                            validators=[DataRequired(), Length(max=140)])
