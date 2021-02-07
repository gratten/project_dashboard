from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AddProjectForm(FlaskForm):
    jobnum = StringField('Job Number', validators=[DataRequired()])
    # prodline = SelectField('Product Line', choices=product_lines, validators=[DataRequired()])
    # serialnum = StringField('Serial Number', validators=[DataRequired()])
    # customer = StringField('Customer', validators=[DataRequired()])
    # description = StringField('Description', validators=[DataRequired()])
    ec_date = StringField('EC Date', validators=[DataRequired()])
    engineer = StringField('Engineer', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddMachineForm(FlaskForm):
    # jobnum = StringField('Job Number', validators=[DataRequired()])
    # prodline = SelectField('Product Line', choices=product_lines, validators=[DataRequired()])
    serialnum = StringField('Serial Number', validators=[DataRequired()])
    # customer = StringField('Customer', validators=[DataRequired()])
    # description = StringField('Description', validators=[DataRequired()])
    # ec_date = StringField('EC Date', validators=[DataRequired()])
    # engineer = StringField('Engineer', validators=[DataRequired()])
    # test_var = 'hello'
    submit = SubmitField('Submit')

class AddKitForm(FlaskForm):
    length = DecimalField('Length', validators=[DataRequired()])
    width = DecimalField('Width', validators=[DataRequired()])
    depth = DecimalField('Depth', validators=[DataRequired()])
    speed = IntegerField('Speed', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddTaskForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    engineer = StringField('Engineer', validators=[DataRequired()])
    submit = SubmitField('Submit')

