# Swipzy - E-Commerce Web Application

Swipzy is a simple e-commerce web application built with **Flask** and **Python**. It allows users to browse products, add items to the cart, and checkout. This project demonstrates basic functionality of an online store with features like login/signup, product browsing, and cart management.

## Features

- **User Authentication**: Users can sign up, log in, and log out.
- **Browse Products**: Users can browse products across categories like Kitchen, Furniture, and Stationery.
- **Add/Remove from Cart**: Users can add products to their shopping cart and remove them when needed.
- **Checkout**: Users can provide delivery details (name, address, phone number) for order processing.
- **Payment Success**: After checkout, users see a payment successful page.

## Tech Stack

- **Frontend**: HTML, CSS (Bootstrap), Jinja2 templates (Flask templating engine)
- **Backend**: Python, Flask framework
- **Database**: In-memory database (Python dictionaries for users and cart data)
- **Version Control**: Git & GitHub

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. Clone the repository:
 git clone https://github.com/tejasvi-sinha23/swipzy.git
2. Navigate to project directory
 cd swipzy
3. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
4. Install the required dependencies:
pip install -r requirements.txt
5. Run the application:
python app.py
The app will be available at http://127.0.0.1:5000/.