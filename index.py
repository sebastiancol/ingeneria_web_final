from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_marshmallow import Marshmallow

# App declaration
app = Flask(__name__)

# REST API config
api = Api(app)
ma = Marshmallow(app)

# Database initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:C0l0mb14++@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Product(db.Model):
    """Product Model"""
    __tablename__ = 'products'

    id_prod = db.Column(db.Integer, primary_key=True)
    name_prod = db.Column(db.String(50))
    price_prod = db.Column(db.Integer)
    quan_prod = db.Column(db.Integer)

    def __repr__(self):
        return '<Product %r>' % self.name

class Category(db.Model):
    """Category Model"""
    __tablename__ = 'category'

    id_cate = db.Column(db.Integer, primary_key=True)
    id_prod = db.Column(db.String(50))
    cate_cate = db.Column(db.String(50))
    descr_cate = db.Column(db.String(50))


    def __repr__(self):
        return '<Category %r>' % self.name

class Sales(db.Model):
    """Sales Model"""
    __tablename__ = 'sales'

    id_sales = db.Column(db.Integer, primary_key=True)
    id_prod = db.Column(db.Integer)

    def __repr__(self):
        return '<Sales %r>' % self.name

class Invoice(db.Model):
    """Invoice Model"""
    __tablename__ = 'invoice'

    id_invoice = db.Column(db.Integer, primary_key=True)
    id_sale = db.Column(db.Integer)
    sale_date = db.Column(db.DateTime)
    sales_value = db.Column(db.Integer)
    id_payment = db.Column(db.Integer)

    def __repr__(self):
        return '<Invoice %r>' % self.name

class Payment(db.Model):
    """Payment Model"""
    __tablename__ = 'payment'

    id_payment = db.Column(db.Integer, primary_key=True)
    type_payment = db.Column(db.Date)
    desc_payment = db.Column(db.Integer)


    def __repr__(self):
        return '<Payment %r>' % self.name


class ProductSchema(ma.Schema):
    """Product Schema"""
    class Meta:
        fields = ('id_prod', 'name_prod', 'price_prod', 'quan_prod')

class CategorySchema(ma.Schema):
    """Category Schema"""
    class Meta:
        fields = ('id_cate', 'id_prod', 'cate_cate', 'desc_cate')

class SalesSchema(ma.Schema):
    """Sales Schema"""
    class Meta:
        fields = ('id_cate', 'id_prod')

class InvoiceSchema(ma.Schema):
    """Invoice Schema"""
    class Meta:
        fields = ('id_invoice','id_sale' , 'sale_date', 'sales_value', 'id_payment')

class PaymentSchema(ma.Schema):
    """Payment Schema"""
    class Meta:
        fields = ('id_payment', 'type_payment', 'desc_payment')


product_schema = ProductSchema()
category_schema = CategorySchema()
sales_schema = SalesSchema()
invoice_schema = InvoiceSchema()
payment_schema = PaymentSchema()
products_schema = ProductSchema(many=True)
categories_schema = CategorySchema(many=True)
saleses_schema = SalesSchema(many=True)
invoices_schema = InvoiceSchema(many=True)
payments_schema = PaymentSchema(many=True)


class IndexView(Resource):
    """Index view"""

    def get(self):
        return {"message": "This is a REST API"}


class UserView(Resource):
    """User view"""

    def get(self):
        """Get all users"""
        users = User.query.all()
        result = users_schema.dump(users)
        return jsonify(result)

    def post(self):
        """Create an user"""
        data = request.get_json()
        user = User(username=data['username'])
        db.session().add(user)
        db.session.commit()

        return {
            "message": "User saved successfully"
        }, 201


api.add_resource(IndexView, '/api')
api.add_resource(UserView, '/api/users')



#MAIN
@app.route('/')
def home():
    return render_template('main.html')

#PRODUCTS
@app.route('/products')
def products():
    return render_template('products.html')

#CATEGORY
@app.route('/category')
def category():
    return render_template('category.html')

#CATEGORY
@app.route('/invoice')
def invoice():
    return render_template('invoice.html')




if __name__ == '__main__':
    app.run(debug=True, port=5000)
