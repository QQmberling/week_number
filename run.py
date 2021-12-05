import datetime

from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import DateField, SubmitField
from wtforms.validators import DataRequired

REFERENCE_DATE = datetime.date(2018, 12, 30)


class DateForm(FlaskForm):
    date = DateField(validators=[DataRequired()])
    submit = SubmitField("Узнать")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.date.data:
            self.date.data = datetime.date.today()


def get_week_number(desire_date, reference_date=REFERENCE_DATE):
    """
    :param desire_date: Желаемая дата, для которой надо узнать номер недели
    :param reference_date: Дата отсчета
    :return: week_number: Номер недели
    """
    amount_of_days = (desire_date - reference_date).days
    if amount_of_days < 0:
        return 1
    return amount_of_days // 7 + 1


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = "you will never guess"


@app.route('/', methods=['POST', 'GET'])
def index():
    form = DateForm()
    date = datetime.date.today()
    if request.method == 'GET':
        form = DateForm()
    elif form.validate_on_submit():
        date = form.date.data
    else:
        return render_template('index.html', form=form, week_number=None)
    week_number = get_week_number(date)
    return render_template('index.html', form=form, week_number=week_number)


if __name__ == '__main__':
    app.run()
