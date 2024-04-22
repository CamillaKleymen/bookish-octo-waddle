from flask import Flask, render_template, request
questions = {"question"}
questions = {}


app = Flask(__name__)
from users import user_bp
from questions import question_bp
app = Flask(__name__)
app.config["CSRF_ENABLED"] = True
app.config["SECRET_KEY"] = "DFgES_54154165#GDfsrdf4442"
app.register_blueprint(user_bp)
app.register_blueprint(question_bp)

@app.route("/question")
def home():
    user_link = "<a href='/user/'>Users</a><br>"
    question_link = "<a href='/question/'>Questions</a><br>"
    return user_link + question_link

@app.route('/', methods=["GET", "POST"]) #url
def hello(): #views
    data = request.args.get("info")
    print(data)
    users = ["Pavel", "Oleg", "Loha"]
    id = '123'
    return render_template("index.html", users=users, id=id)
@app.route("/add-question", methods=["GET", "POST"] )
def questions():
    global question
    front_question = request.form.get("question")
    front_main_text = request.form.get("main_text")
    question[front_question]= {"question": front_question,
                                "main_text": front_main_text,
                                "answer": []}
    print(front_question, front_main_text)
    return render_template("question.html",
                           exact_question=question[front_question])
# create dinamic url
@app.route("/<int:pk>", methods=["GET", 'POST'])
def test(pk):
    return str(pk)

app.run(debug=True)