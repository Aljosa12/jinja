from flask import Flask, render_template, request, make_response

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
    priimek = request.form.get("last-name")
    geslo = request.form.get("geslo")
    response = make_response(
        render_template(
            "response.html", priimek=priimek, user=ime, geslo=geslo)
    )
    response.set_cookie("ime", ime)
    response.set_cookie("priimek", priimek)
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
