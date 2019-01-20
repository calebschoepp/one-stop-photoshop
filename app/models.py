from app import app, db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    folder = db.Column(db.String(100), index=True, unique=True)
    image_count = db.Column(db.Integer, index=True)

    def __repr__(self):
        return "<Post in {} with {} images>".format(self.folder, self.image_count)
