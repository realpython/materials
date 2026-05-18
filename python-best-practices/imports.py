# Avoid this:
# from app.utils.helpers import format_date, slugify
# import requests, os, sys
# from .models import *
# import json

# def get_data():
#     # Call the API here...

# def build_report(data):
#     # Generate report here...


# Favor this:
# import json
# import os
# import sys

# import requests

# from app.utils import helpers
# from . import models

# def get_data():
#     # Call the API here...

# def build_report(data):
#     # Generate report here...
