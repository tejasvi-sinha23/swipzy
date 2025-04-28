from flask import Flask, render_template, request, redirect, url_for, session
from models import User, Admin, Product, Cart  # Import OOPS models
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Temporary in-memory "database"
users = {}
products = [
    Product("Notebook", 5, "Stationery", "notebook.jpg"),
    Product("Pen", 2, "Stationery", "pen.jpg"),
    Product("Mixer Grinder", 70, "Kitchen", "mixer.jpg"),
    Product("Chair", 45, "Furniture", "chair.jpg"),
    Product("Tawa", 15, "Kitchen", "tawa.jpg"),
    Product("Bookshelf", 120, "Furniture", "bookshelf.jpg"),
    Product("Table", 80, "Furniture", "table.jpg"),
    Product("Cutting Board", 15, "Kitchen", "cutting_board.jpg"),
    Product("Knife Set", 30, "Kitchen", "knife_set.jpg"),
    Product("Pan", 25, "Kitchen", "pan.jpg"),
    Product("Highlighter", 2, "Stationery", "highlighter.jpg"),
    Product("Sofa", 200, "Furniture", "sofa.jpg")
]

carts = {}

# ---------------- Home Page ----------------
@app.route('/')
def home():
    return render_template('home.html')

# ---------------- Signup Page ----------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return "User already exists! Try logging in."
        users[username] = User(username, password)  # Encapsulation
        return redirect(url_for('login'))
    return render_template('signup.html')

# ---------------- Login Page ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user.verify_password(password):  # Encapsulation
            session['user'] = username
            if username not in carts:
                carts[username] = Cart()
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Credentials!"
    return render_template('login.html')

# ---------------- Dashboard Page ----------------
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    user = session['user']
    # Recommend first 3 products
    recommended = products[:3]
    return render_template('dashboard.html', user=user, recommended=recommended)

# ---------------- Browse Products ----------------
@app.route('/browse', methods=['GET', 'POST'])
def browse():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    search_query = request.args.get('search', '')
    filtered_products = products
    
    # If a search query is provided, filter the products based on name or category
    if search_query:
        search_query = search_query.lower()
        filtered_products = [
            p for p in products if search_query in p.name.lower() or search_query in p.category.lower()
        ]
    
    return render_template('browse.html', products=filtered_products)


# ---------------- Add to Cart ----------------
@app.route('/add_to_cart/<product_name>')
def add_to_cart(product_name):
    if 'user' not in session:
        return redirect(url_for('login'))
    user_cart = carts.get(session['user'])
    product = next((p for p in products if p.name == product_name), None)
    if product:
        user_cart.add_item(product)
    # Prevent redirect to the cart page
    return redirect(url_for('browse'))

# ---------------- Remove from Cart ----------------
@app.route('/remove_from_cart/<product_name>')
def remove_from_cart(product_name):
    if 'user' not in session:
        return redirect(url_for('login'))
    user_cart = carts.get(session['user'])
    product = next((p for p in products if p.name == product_name), None)
    if product:
        user_cart.remove_item(product)  # Remove item from the cart
    return redirect(url_for('cart'))

# ---------------- Checkout Page ----------------
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Handle the form submission
        name = request.form['name']
        address = request.form['address']
        phone = request.form['phone']
        
        # Here you can implement actual payment logic (this is a placeholder)
        
        # After successful submission, redirect to the payment success page
        return redirect(url_for('payment_successful', name=name))

    return render_template('checkout.html')

# ---------------- View Cart ----------------
@app.route('/cart')
def cart():
    if 'user' not in session:
        return redirect(url_for('login'))
    user_cart = carts.get(session['user'])
    total = user_cart.total_price() if user_cart else 0
    return render_template('cart.html', cart=user_cart.view_cart(), total=total)

# ---------------- Logout ----------------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

# ---------------- Payment Successful Page ----------------
@app.route('/payment_successful')
def payment_successful():
    name = request.args.get('name')
    return render_template('payment_successful.html', name=name)

# ----------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True) 