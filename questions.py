from flask import Blueprint
#create an object of component
question_bp = Blueprint('question', __name__, url_prefix="/question")

@question_bp.route("/")
def question():
    return "Hello from questions"