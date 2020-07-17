@main.route("/login")
def login():
    return render_template("login.html")

@main.route("/register")
def question():
    return render_template("register.html")
