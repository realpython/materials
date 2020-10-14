from flask import Blueprint
from flask import render_template
from app import db
from app.models import Employee


# Setup the Blueprint
employees_bp = Blueprint(
    "employees_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@employees_bp.route("/employees", methods=["GET"])
@employees_bp.route("/employees/<int:employee_id>", methods=["GET"])
def employees(employee_id=None):

    # Start the query for employees
    query = db.session.query(Employee)

    # Display the employee for the employee id passed?
    if employee_id is not None:
        query = query.filter(Employee.employee_id == employee_id)

    employees = query.order_by(Employee.employee_id).all()

    return render_template("employees.html", employees=employees)
