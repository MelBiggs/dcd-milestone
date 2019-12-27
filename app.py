import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGODB_NAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.secret_key = "dfsgfgdf"
mongo = PyMongo(app)


@app.route('/')
@app.route('/get_users')
def get_users():
    return render_template("users.html", users=mongo.db.users.find())

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = mongo.db.users.find_one({"email": email})

        if (not user):
            return "incorrect login details"

        if (not check_password_hash(user["password"], password)):
            return "incorrect login details"

        session["user"] = user["username"]

        return redirect("get_users")

    return render_template("login.html")

@app.route("/logout", methods=["GET"])
def logout():
    username = session["user"]
    user = mongo.db.users.find_one({"username": username})
    session.pop("user")
    return redirect("get_users")

@app.route('/register', methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        dob = request.form.get("dob")
        
        if (mongo.db.users.find_one({"username": username})):
            return "existing user"

        if (mongo.db.users.find_one({"email": email})):
            return "existing email"

        password = generate_password_hash(request.form.get("password"))
        
        mongo.db.users.insert_one({"username": username, "email":email, "password":password, "dob":dob})
        
        # Creates a cookie to store logged in user
        session["user"] = username

        return redirect("get_users")
    return render_template("registration.html")


# execute app__init__.py
if __name__ == '__main__':

    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
