from flask import Flask, request, jsonify
import jwt
from functools import wraps
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password321'  # Replace with a strong, secret key

# Simulated database for user storage
users_db = {}
products_db = {}

# ...

# New route to get all registered users
@app.route('/users', methods=['GET'])
def get_all_users():
    all_users = list(users_db.keys())
    return jsonify(all_users)


# Authentication decorator to protect routes
def authenticate_user(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token:
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
                if data['username'] in users_db:
                    return f(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 401
            except jwt.InvalidTokenError:
                pass  # Token is invalid

        return jsonify({'message': 'Authentication required'}), 401

    return decorated

# User registration endpoint
@app.route('/users/register', methods=['POST'])
def register_user():
    data = request.get_json()
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']

        if username in users_db:
            return jsonify({'message': 'User already exists'}), 400
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            users_db[username] = hashed_password
            return jsonify({'message': 'User registered successfully'}), 201
    else:
        return jsonify({'message': 'Invalid registration data'}), 400

# User login endpoint
@app.route('/users/login', methods=['POST'])
def login_user():
    data = request.get_json()
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']

        if username in users_db and bcrypt.checkpw(password.encode('utf-8'), users_db[username]):
            token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({'token': token})
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    else:
        return jsonify({'message': 'Invalid login data'}), 400

# A protected route for authenticated users
@app.route('/protected', methods=['GET'])
@authenticate_user
def protected_route():
    return jsonify({'message': 'This is a protected route for authenticated users'})


# New route to get all registered products
@app.route('/products', methods=['GET'])
def get_all_products():
    all_products = list(products_db.keys())
    return jsonify(all_products)

# Product registration endpoint
@app.route('/products/register', methods=['POST'])
def register_Product():
    data = request.get_json()
    if 'productid' in data and 'productname' in data:
        productid = data['productid']
        productname = data['productname']
        productprice = data['productprice']
        productdescription = data['productdescription']

        if productid in products_db:
            return jsonify({'message': 'Product already exists'}), 400
        else:
            products_db[productid] = data
            return jsonify({'message': 'Product registered successfully'}), 201
    else:
        return jsonify({'message': 'Invalid registration data'}), 400

# Product deletion endpoint
@app.route('/products/delete', methods=['DELETE'])
def delete_product():
    data = request.get_json()
    if 'productid' in data:
        productid = data['productid']

        if productid in products_db:
            # Delete the Product from the database
            del products_db[productid]
            return jsonify({'message': 'Product deleted successfully'}), 200
        else:
            return jsonify({'message': 'Product not found'}), 404
    else:
        return jsonify({'message': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=5002)
