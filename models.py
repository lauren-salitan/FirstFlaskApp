from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# attempted soluton:
# def get_pet_by_id(id):
#     """Get a pet by ID using a session."""
#     return db.session.get(Pet, id)



# models go below

class Pet(db.Model):
    """Pet."""
    __tablename__ = "pets"

    @classmethod
    def get_by_species(cls, species):
        return cls.query.filter_by(species=species).all()
    
    @classmethod
    def get_all_hungry(cls):
        return cls.query.filter(Pet.hunger >20).all()

    @classmethod
    def get_pet_by_id(pet_id):
        """Get a pet by ID using a session."""
        return db.session.execute(db.select(Pet).filter_by(id=pet_id)).scalar()
 
    def __repr__(self):
        p=self
        return f"<Pet id={p.id} name={p.name} species={p.species} hunger={p.hunger}"
    # def __repr__(self):
    #     return f"<Pet id={self.id} name={self.name} species={self.species} hunger={self.hunger}>"

    

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)

    species = db.Column(db.String(30), 
                        nullable=True)

    hunger = db.Column(db.Integer, 
                       nullable=False, 
                       default=20)
    def greet(self):
        return f"Hi, I am {self.name}, the {self.species}"
    def feed(self, amt=20):
        """update hunger based off amount"""
        self.hunger -= amt
        self.hunger = max(self.hunger, 0)




##### attempt
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# def connect_db(app):
#     db.app = app
#     db.init_app(app)

# # Util function to get a pet by name
# def get_pet_by_name(name):
#     """Get a pet by name using a session."""
#     return Pet.query.filter_by(name=name).first()

# # models go below

# class Pet(db.Model):
#     """Pet."""
#     __tablename__ = "pets"

#     @classmethod
#     def get_by_species(cls, species):
#         return cls.query.filter_by(species=species).all()
    
#     @classmethod
#     def get_all_hungry(cls):
#         return cls.query.filter(Pet.hunger > 20).all()

#     def __repr__(self):
#         return f"<Pet id={self.id} name={self.name} species={self.species} hunger={self.hunger}>"

#     id = db.Column(db.Integer,
#                    primary_key=True,
#                    autoincrement=True)
#     name = db.Column(db.String(50),
#                      nullable=False,
#                      unique=True)
#     species = db.Column(db.String(30), 
#                         nullable=True)
#     hunger = db.Column(db.Integer, 
#                        nullable=False, 
#                        default=20)

#     def greet(self):
#         return f"Hi, I am {self.name}, the {self.species}"

#     def feed(self, amt=20):
#         """Update hunger based off amount fed."""
#         self.hunger -= amt
#         self.hunger = max(self.hunger, 0)
#####
    
# kyle = Pet(name="kyle the chicken", species="Chicken")
# kyle.name="Kyle The Rooster"

# kyle.getOffspring()

# CREATE TABLE pets {
#     id abjhe
#     name hjsdb
#     pecies jhdb
# }


