from flask import Blueprint, request, jsonify
from crypto.kyber_utils import encrypt, decrypt
from crypto.dilithium_utils import sign, verify

message_routes = Blueprint('messages', __name__)

@message_routes.route('/api/messages', methods=['POST'])
def send_message():
    data = request.json
    ciphertext = encrypt(data['recipient_pub'], data['message'])
    signature = sign(data['sender_priv'], ciphertext)
    return jsonify({"ciphertext": ciphertext, "signature": signature})

@message_routes.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify({"messages": []})
