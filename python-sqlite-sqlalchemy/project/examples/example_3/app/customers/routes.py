from flask import Blueprint
from flask import render_template
from sqlalchemy import func
from app import db
from app.models import Customer
from app.models import Invoice
from sqlalchemy import desc


# Setup the Blueprint
customers_bp = Blueprint(
    "customers_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@customers_bp.route("/customers", methods=["GET"])
@customers_bp.route("/customers/<int:customer_id>", methods=["GET"])
def customers(customer_id=None):

    # Start the query for customers
    query = db.session.query(
        Customer, func.sum(Invoice.total).label("invoices_total")
    ).join(Invoice)

    # Display the albums for the customer passed?
    if customer_id is not None:
        query = query.filter(Customer.customer_id == customer_id)

    results = (
        query.group_by(Customer.customer_id)
        .order_by(desc(func.sum(Invoice.total)))
        .all()
    )
    return render_template("customers.html", results=results)
