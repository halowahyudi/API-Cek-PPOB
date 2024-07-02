from flask import blueprints
from src.telkomIndihome import telkomIndihome

telkomIndihomeInquiriess = blueprints.Blueprint('telkomIndihomeInquiriess', __name__)


@telkomIndihomeInquiriess.route('/api/telkomIndihomeInquiries/', methods=['GET'])
def index():
    return {
        "status": False,
        "message": "Customer number cannot be empty"
    }, 404


@telkomIndihomeInquiriess.route('/api/telkomIndihomeInquiries/<customer_number>', methods=['GET'])
def get_data(customer_number):
    try:
        return telkomIndihome(customer_number)._get_data()

    except Exception:

        return {
            "status": False,
            "message": "Server error"
        }, 500
