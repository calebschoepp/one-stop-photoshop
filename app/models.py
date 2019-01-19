from app import app, db
# from datetime import datetime

# class Game(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(140), index=True, unique=True)
#     review = db.Column(db.String(300))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

#     def __repr__(self):
#         return "<Game '{}'>".format(self.name)

# class Play(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     note = db.Column(db.String(300))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     date = db.Column(db.Date, index=True)
#     game_id = db.Column(db.Integer, db.ForeignKey('game.id'))

#     def __repr__(self):
#         return "<Play on {}>".format(self.date)
