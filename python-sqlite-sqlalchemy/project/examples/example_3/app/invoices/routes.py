from flask import Blueprint
from flask import render_template
from app import db
from app.models import Invoice


# Setup the Blueprint
invoices_bp = Blueprint(
    "invoices_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@invoices_bp.route("/invoices", methods=["GET"])
@invoices_bp.route("/invoices/<int:invoice_id>", methods=["GET"])
def invoices(invoice_id=None):
    # Start the query for invoices
    query = db.session.query(Invoice)

    # Display the invoice for the invoice id passed?
    if invoice_id is not None:
        query = query.filter(Invoice.invoice_id == invoice_id)

    invoices = query.order_by(Invoice.invoice_id).all()
    return render_template("invoices.html", invoices=invoices)
