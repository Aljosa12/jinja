from flask import Flask, render_template, request, make_response, url_for
from models import User, db

db.create_all()

app = Flask(__name__)

@app.route("/")
def base():
    user = get_user()
    return render_template("home.html", user=user)

@app.route("/login", methods=["GET"])
def on_about():
    user = get_user()
    return render_template("login.html", user=user)

@app.route("/login", methods=["POST"])
def on_about_post():
    ime = request.form.get("vnos-imena")
    email = request.form.get("email")
    geslo = request.form.get("geslo")

    user = User(email=email, user=ime, geslo=geslo)

    db.add(user)
    db.commit()

    response = make_response(
        redirect(url_for(
        ))
    )

    return response

@app.route("/logout")
def logout():
    response = make_response(render_template("logout.html"))
    response.set_cookie("ime", "", expires=0)
    response.set_cookie("priimek", "", expires=0)
    return response

def get_user():
    return request.cookies.get("username")


if __name__ == "__main__":
    app.run()
