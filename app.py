# # BEFORE:
# from flask import Flask, request, render_template,  redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'
# # db=SQLAlchemy(app)
# db = SQLAlchemy()
# db.app = app
# db.init_app(app)

# app.config['SECRET_KEY'] = "chickenzarecool21837"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

# @app.route('/')
# def home_page():
#     """Shows home page"""
#     return render_template('home.html')

#####


# # AFTER:
from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet#, get_pet_by_id

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] =  True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_pets():
    """Shows list of all pets in db"""
    pets = Pet.query.all()
    return render_template('list.html', pets=pets)

#video:
# @app.route('/<int:pet_id>')
# def show_pet(pet_id):
#     """show details"""
#     pet = Pet.query.get(pet_id)
#     return f"<h1>{{pet.name}}</h1>"

#solution attempt 4:
# @app.route('/<int:pet_id>')
# def show_pet(pet_id):
#     """show details"""
#     pet = get_pet_by_id(id)
#     return f"<h1>{{pet.name}}</h1>"
# #     # return f"<h1>(pet.name)</h1>"

#solution #5
# @app.route('/<int:pet_id>')
# def show_pet(pet_id):
#     """show details"""
#     pet = db.session.execute(db.select(Pet).filter_by(id=pet_id)).scalar()
#     return f"<h1>{{pet.name}}</h1>"
#     # return f"<h1>(pet.name)</h1>"

 #solution #6
@app.route('/<int:pet_id>')
def show_pet(pet_id):
    """show details"""
    return f"<h1>{db.session.execute(db.select(Pet).filter_by(id=pet_id)).scalar().name}</h1>"
    # return f"<h1>(pet.name)</h1>"   

###Video later on:
# @app.route('/', methods=["POST"])
# def create_pet():
#     name = request.form["name"]
#     species = request.form["species"]
#     hunger = request.form["hunger"]
#     hunger = int(hunger) if hunger else None

#     new_pet  = Pet(name=name, species=species, hunger=hunger)
#     db.session.add(new_pet)
#     db.session.commit()

#     return redirect(f'/{new_pet.id}')

# @app.route("/<int:pet_id>")
# def show_pet(pet_id):
#     """Show details about a single pet"""
#     pet = Pet.query.get_or_404(pet_id)
#     return render_template("details.html", pet=pet)

# @app.route("/species/<species_id>")
# def show_pets_by_species(species_id):
#     pets = Pet.get_by_species(species_id)
#     return render_template("species.html", pets=pets, species=species_id)
###

# # #attempt
# # @app.route('</int:pet_id>')
# # def show_pet(pet_id):
# #     """show details"""
# #     pet = db.session.get(Pet, id)
# #     return f"<h1>(pet.name)</h1>"

# # attempt 2
# @app.route('</int:pet_name>')
# def show_pet(pet_name):
#     """show details"""
#     pet = Pet.query.filter_by(name=pet_name).first
#     return f"<h1>(pet.name)</h1>"





##### attempt 3
# from flask import Flask, request, render_template, redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
# from models import db, connect_db, Pet, get_pet_by_name

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
# app.config['SECRET_KEY'] = "chickenzarecool21837"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

# connect_db(app)

# @app.route('/')
# def list_pets():
#     """Shows list of all pets in db"""
#     pets = Pet.query.all()
#     return render_template('list.html', pets=pets)

# @app.route('/pet/<name>')
# def show_pet(name):
#     """show details of a pet with given name"""
#     pet = get_pet_by_name(name)
#     if pet:
#         return f"<h1>{pet.name}</h1>"
#     else:
#         return "<h1>Pet not found!</h1>"

#####







# @app.route('/<int:pet_id>')
# def show_pet(pet_id):
#     """show details of a pet with given ID"""
#     pet = get_pet_by_id(pet_id)
#     if pet:
#         return f"<h1>{pet.name}</h1>"
#     else:
#         return "<h1>Pet not found!</h1>"

# if __name__ == '__main__':
#     with app.app_context():
#         print("Database URL:", db.engine.url)
#     app.run()


# from flask import Flask, request, render_template, redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Set configuration before initializing the SQLAlchemy object
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'
# app.config['SECRET_KEY'] = "chickenzarecool21837"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# # Initialize SQLAlchemy with the app
# db = SQLAlchemy(app)

# # Initialize DebugToolbarExtension with the app
# debug = DebugToolbarExtension(app)

# @app.route('/testdb')
# def test_db():
#     try:
#         # Getting a connection and executing a query
#         with db.engine.connect() as connection:
#             result = connection.execute('SELECT 1')
#             return str(result.fetchone())
#     except Exception as e:
#         return str(e)

# if __name__ == "__main__":
#     app.run(debug=True)