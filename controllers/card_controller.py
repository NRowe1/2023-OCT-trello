from flask import Blueprint
from init import db
from models.card import Card

cards_dp = Blueprint('cards',__name__, url_prefix='/cards')

@cards_dp.route('/')
def get_all_cards():
    stmt = db.select(Card).order_by(Card.date.desc())
    cards = db.session.scalars(stmt)
    return cards_schema.dump(cards)