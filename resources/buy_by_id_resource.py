from flask_login import current_user
from flask_restful import Resource

from app import Ticket, User
from app import Transaction
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

class BuyByIDRasource(Resource):
    @jwt_required
    def get(self, id):
        current_user_name = get_jwt_identity()
        current_user = User.query.filter_by(username=current_user_name).first()

        transaction = Transaction.query.filter_by(id=id, booked=False).first()
        if transaction is None:
            return "transaction not exist", 404
        ticket = Ticket.query.filter_by(id=transaction.ticket_id).first()

        return {
            "id": ticket.id,
            "place": ticket.seat,
            "price": ticket.price,
            "title": ticket.title,
            "date": ticket.date
        }
