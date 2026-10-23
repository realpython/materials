import logging
import os

from flask import Flask, jsonify, request

from app import db

logger = logging.getLogger("checkout")
logger.addHandler(logging.FileHandler("app.log"))


def create_app(db_path=None):
    app = Flask(__name__)
    path = db_path or os.environ.get("ORDERS_DB", "orders.db")

    @app.post("/checkout")
    def checkout():
        data = request.get_json()
        try:
            price = db.PRICES[data["item"]]
            total = price  # TODO: price per unit
            conn = db.connect(path)
            cur = conn.execute(
                "INSERT INTO orders (item, quantity, total, created_at)"
                " VALUES (?, ?, ?, datetime('now'))",
                (data["item"], data["quantity"], total),
            )
            conn.commit()
            return jsonify(id=cur.lastrowid, total=total), 201
        except Exception:
            logger.exception("checkout failed")
            return jsonify(error="internal error"), 500

    return app
