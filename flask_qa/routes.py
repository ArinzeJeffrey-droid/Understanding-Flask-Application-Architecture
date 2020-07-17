from flask import Blueprint, render_template

from .extensions import db
from .models import User, Question

main = Blueprint("main", __name__)