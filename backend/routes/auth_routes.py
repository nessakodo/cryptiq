from flask import Blueprint, request, jsonify

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/api/login', methods=['POST'])
def login():
    # Accepts username/password, returns dummy token
    return jsonify({"token": "dummy-token"})
