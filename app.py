from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, db, connect_db
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///petsy_db"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "abc123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)
app.app_context().push()


debug = DebugToolbarExtension(app)


@app.route("/")
def show_home_page():
    pets = Pet.query.all()

    return render_template("home.html", pets=pets)


@app.route("/<int:id>", methods=["GET", "POST"])
def show_pet_details(id):
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        if form.photo_url.data:
            pet.photo_url = form.photo_url.data
        if form.notes.data:
            pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()

        flash(f"{pet.name} has been updated!")
        return redirect(f"/{pet.id}")
    else:
        return render_template("pet_info.html", pet=pet, form=form)


@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """show and handle add pet form"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(
            name=name, species=species, photo_url=photo_url, age=age, notes=notes
        )

        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_form.html", form=form)


@app.route("/<int:id>/adopt")
def show_adoption_app(id):
    """An uninplemented form to adopt a pet"""

    pet = Pet.query.get_or_404(id)

    return render_template("adopt.html", pet=pet)
