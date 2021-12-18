from flask import render_template, url_for
from Ecommerce.models import Products
from Ecommerce import app, db


@app.route('/')
@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', title='The TECH SHOP | E commerce Website')


@app.route('/PDB', methods=['GET', 'POST'])
def table():
    products = Products.query.all()
    print(products)
    return render_template('Ptable.html', title='Products DB | The TECH SHOP', Products=products)

    
@app.route('/LoginSignUp', methods=['GET', 'POST'])
def LSP():
    return render_template('LSP.html', title='Login-SignUp | The TECH SHOP')


@app.route('/AboutUs', methods=['GET'])
def AboutUs():
    return render_template('aboutus.html', title='About Us | The TECH SHOP')


@app.route('/Billing', methods=['GET', 'POST'])
def Bill():
    return render_template('Bill.html', title='Billing | The TECH SHOP')


@app.route('/404', methods=['GET'])
def Er404():
    return render_template('Error404.html', title='Error404 | The TECH SHOP')


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    return render_template('cart.html', title='Cart | The TECH SHOP')


@app.route('/checkout', methods=['GET', 'POST'])
def cckout():
    return render_template('cckout.html', title='Checkout | The TECH SHOP')


@app.route('/FAQ', methods=['GET', 'POST'])
def FAQ():
    return render_template('faq.html', title='FAQ | The TECH SHOP')


@app.route('/Offers', methods=['GET'])
def Offers():
    return render_template('offers.html', title='Offers | The TECH SHOP')


@app.route('/products-page-1', methods=['GET', 'POST'])
def products():
    return render_template('products.html', title='Products Page 1 | The TECH SHOP')


@app.route('/products-page-2', methods=['GET'])
def pg2():
    return render_template('pg-2.html', title='Products Page 2 | The TECH SHOP')


products = [
    {
        'name': 'boAt Rockerz 518',
        'price': 1599.00,
        'image_file1': 'main page\\tufgaming1.png',
    },
    {
        'name': 'boAt Stone 650R',
        'price': 111599.00,
        'image_file1': 'main page\\tufgaming1.png',
    },
    {
        'name': 'boAt Rockerz 610',
        'price': 1999.00,
        'image_file1': 'main page\\tufgaming1.png',
    },
    {
        'name': 'JBL Tune 165BT',
        'price': 111912.00,
        'image_file1': 'main page\\tufgaming1.png',
    },
    {
        'name': 'DELL Alienware  m15(R3)',
        'price': 219990.00,
        'image_file1': 'main page\\tufgaming1.png',
    },
    {
        'name': 'ASUS TUF GAMING F15',
        'price': 89_249.00,
        'specs': 'ASUS TUF F15 Gaming FX506LI-HN222TS I7 i7-10870H/ GTX1650Ti-4GB/ 8G/ 1T HDD+512G SSD/ 15.6 FHD-144hz/ RGB Backlit/ WIFI6/ 48Wh/ WIN10/ Bonfire Black/ Office Home & Student 2019',
        'image_file1': 'main page\\tufgaming1.png',
        'image_file2': 'laptops\\tuf gaming\\2.png',
        'image_file3': 'laptops\\tuf gaming\\3.png',
        'image_file4': 'laptops\\tuf gaming\\tufgaming2.jpg'
    },
]


@app.route('/prodtemp', methods=['GET', 'POST'])
def prodtemp():
    return render_template('prodtemp.html', title='temp testing', products=products)


@app.route('/indprodtemp', methods=['GET', 'POST'])
def indprodtemp():
    id = 5
    product = products[id]
    relprods = [p for p in products if p['price'] > 50000]  # and p['id']!=id]
    relprods = relprods[:3]
    print(relprods)
    # if request.method == 'POST':
    #     quantity = request.form['quantity']

    return render_template('indprodtemp.html', title='ind temp testing', product=product, relprods=relprods)
