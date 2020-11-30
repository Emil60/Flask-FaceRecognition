from flskfaceapp import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    images = db.relationship('Images',backref='user', lazy=True)
    
    def __init__(self, name):
        self.name = name

class Images(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    photo_location = db.Column(db.PickleType, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),nullable = False)

    def __init__(self, photo_location, user_id):
        self.photo_location = photo_location
        self.user_id = user_id