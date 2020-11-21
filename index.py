from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_migrate import Migrate
import psycopg2
import os

# App declaration
app = Flask(__name__)

# REST API config
api = Api(app)
ma = Marshmallow(app)

# Database initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:C0l0mb14++@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.secret_key = "secret"


class Product(db.Model):
    """Product Model"""
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    # sales= db.relationship("Sales", back_populates="sales")

    def __repr__(self):
        return '<Product %r>' % self.name


class Category(db.Model):
    """Category Model"""
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    product = db.relationship("Product", backref="products")

    def __repr__(self):
        return '<Category %r>' % self.name


'''
class Sales(db.Model):
    """Sales Model"""
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    invoices= db.relationship("Invoice", back_populates="invoice")

    def __repr__(self):
        return '<Sales %r>' % self.name

class Invoice(db.Model):
    """Invoice Model"""
    __tablename__ = 'invoice'

    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sales.id'))
    sale_date = db.Column(db.DateTime)
    sales_value = db.Column(db.Integer)
    payment_id= db.Column(db.Integer, db.ForeignKey('payment.id'))


    def __repr__(self):
        return '<Invoice %r>' % self.name

class Payment(db.Model):
    """Payment Model"""
    __tablename__ = 'payment'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Date)
    desc = db.Column(db.Integer)
    invoices= db.relationship("Invoice", back_populates="invoice")


    def __repr__(self):
        return '<Payment %r>' % self.name

'''

# MAIN


@app.route('/')
def home():
    return render_template('store.html')

# PRODUCTS


@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)


@app.route('/add_product', methods=['POST'])
def create_product():
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            price=request.form['price'],
            quantity=request.form['quantity'],
        )
        db.session.add(product)
        db.session.commit()
        flash('Se ha guardado el producto correctamente.')
        return redirect(url_for("products"))


@app.route('/delete_product/<string:id>')
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    flash('Producto eliminado.')
    return redirect(url_for("products"))


@app.route('/edit_product/<string:id>', methods=['POST', 'GET'])
def edit_product(id):
    product = Product.query.get(id)
    if request.method == 'GET':
        return render_template("edit_product.html", product=product)
    else:
        product.name =name=request.form['name']
        product.price=request.form['price']
        product.quantity=request.form['quantity']
        db.session.commit()
        flash('Producto actualizado.')
        return redirect(url_for("products"))


# CATEGORY
@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/create_category')
def create_category():
    return render_template('create_categories.html')

'''
@app.route('/add_category', methods=['POST'])
def create_product():
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            price=request.form['price'],
            quantity=request.form['quantity'],
        )
        db.session.add(product)
        db.session.commit()
        flash('Se ha guardado el producto correctamente.')
        return redirect(url_for("category"))


@app.route('/delete_category/<string:id>')
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    flash('Producto eliminado.')
    return redirect(url_for("category"))


@app.route('/edit_category/<string:id>', methods=['POST', 'GET'])
def edit_product(id):
    product = Product.query.get(id)
    if request.method == 'GET':
        return render_template("edit_category.html", category=category)
    else:
        product.name =name=request.form['name']
        product.description=request.form['price']
        #product.quantity=request.form['quantity']
        db.session.commit()
        flash('Categoria actualizado.')
        return redirect(url_for("category"))
'''

# invoice


@app.route('/invoice')
def invoice():
    return render_template('invoice.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
