from Ecommerce import db


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Products(db.Model):
    prod_id = db.Column(db.Integer, primary_key=True)
    prodname = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    Specs = db.Column(db.String(5000), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    path1 = db.Column(db.String(100), nullable=False)
    path2 = db.Column(db.String(100), nullable=False)
    path3 = db.Column(db.String(100), nullable=False)
    path4 = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Products('{self.prodname}', '{self.price}', '{self.type}' , '{self.path1}', '{self.path2}', '{self.path3}', '{self.path4}')"

