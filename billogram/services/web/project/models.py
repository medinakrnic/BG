from . import db


class DiscountCodes(db.Model):
    __tablename__ = "discount_codes"
    code_id = db.Column(db.Integer, primary_key=True)
    discount_code = db.Column(db.String, unique=False, nullable=False)
    discount_value = db.Column(db.Integer, unique=False, nullable=False)
    user_claimed = db.Column(db.Integer, unique=True, nullable=True)


class Users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=False, nullable=False)
    name = db.Column(db.String, unique=False, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    discount_code = db.Column(db.Integer, unique=True, nullable=True)
