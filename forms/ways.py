from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class WaysForm(FlaskForm):
    way = StringField('Описание', validators=[DataRequired()])
    work_size = IntegerField('Длительность', validators=[DataRequired()])
    leader = StringField('Название', validators=[DataRequired()])
    start_date = StringField('Дата начала')
    end_date = StringField('Дата окончания')
    is_finished = BooleanField("Is finished")
    categor = IntegerField('Категория')
    iname = StringField('Город улица дом')
    submit = SubmitField('Добавить')