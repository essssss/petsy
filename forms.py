from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    FloatField,
    BooleanField,
    IntegerField,
    RadioField,
    SelectField,
)
from wtforms.validators import InputRequired, Email, URL, Optional


class AddPetForm(FlaskForm):
    """A form to add a pet"""

    name = StringField("Pet's Name", validators=[InputRequired()])
    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
        validators=[InputRequired()],
    )
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField("Animal's Age", validators=[Optional()])
    notes = StringField("Notes about this pet", validators=[Optional()])


class EditPetForm(FlaskForm):
    """a form to edit a pet"""

    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    notes = StringField("Notes about this pet", validators=[Optional()])
    available = BooleanField("Is this Pet Available for adoption?")
