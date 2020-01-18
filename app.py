import os
from flask import (
    Flask, render_template, redirect,
    request, flash, url_for, session,
    Markup)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGODB_NAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)


@app.route('/')
def home():
    """ Home page with recipe of the day """
    return render_template("index.html")


@app.route('/get_users')
def get_users():
    return render_template("users.html", users=mongo.db.users.find())


# Log in / Log Out / Register

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
            flash(Markup("<h4>\
            {request.form.get('username')}\
            is already taken! Please try again.</h4>"))

        if (mongo.db.users.find_one({"email": email})):
            return "existing email"

        password = generate_password_hash(request.form.get("password"))

        mongo.db.users.insert_one(
            {"username": username, "email": email, "password": password, "dob": dob})

        # Creates a cookie to store logged in user
        session["user"] = username

        return redirect("get_users")
    return render_template("registration.html")


# Recipes CRUD
@app.route('/recipes', methods=['GET'])
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


@app.route('/recipes/<recipe_id>', methods=['GET'])
def view_recipe(recipe_id):
    return render_template("show_recipe.html",
        categories=mongo.db.categories.find(),
        recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})) 

@app.route('/recipes/create', methods=['GET', 'POST'])
def create_recipe():
    if request.method == "POST":

        data = request.form.to_dict()

        if (mongo.db.recipes.find_one({"name": data['name']})):
            return "Existing recipe"

            # Getting the list of ingredients and delete the incorrect data placeholder
        data.update({'ingredients': request.form.getlist('ingredients[]')})
        del data['ingredients[]']

        data.update({'steps': request.form.getlist('steps[]')})
        del data['steps[]']
        
        mongo.db.recipes.insert_one(data)
        return redirect(url_for("get_recipes"))
        
    categories = mongo.db.categories.find()
    return render_template("create_recipes.html", recipe={}, categories=categories)


@app.route('/recipes/edit/<recipe_id>', methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        recipes = mongo.db.recipes
        data = request.form.to_dict()
        data.update({'ingredients': request.form.getlist('ingredients[]')})
        del data['ingredients[]']

        data.update({'steps': request.form.getlist('steps[]')})
        del data['steps[]']

        recipes.update({"_id": ObjectId(recipe_id)}, data)

        return redirect(url_for("get_recipes"))
    categories = mongo.db.categories.find()
    return render_template("edit_recipes.html", categories=categories, recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}))


@app.route("/recipes/delete/<recipe_id>", methods=['GET'])
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for("get_recipes"))


# Categories

@app.route('/categories', methods=["GET"])
def get_categories():
    return render_template("categories.html", categories=mongo.db.categories.find())


@app.route('/categories/create', methods=["GET", "POST"])
def create_category():
    if request.method == "POST":
        name = request.form.get("name")

        if (mongo.db.categories.find_one({"name": name})):
            return "existing category"

        mongo.db.categories.insert_one({"name": name})
        return redirect(url_for("get_categories"))

    return render_template("create_categories.html", category={})


@app.route('/categories/edit/<category_id>', methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        name = request.form.get("name")

        if (mongo.db.categories.find_one({"name": name})):
            return "existing category"

        categories = mongo.db.categories
        categories.update({"_id": ObjectId(category_id)}, {"name": name})

        return redirect(url_for("get_categories"))

    return render_template("edit_categories.html", category=mongo.db.categories.find_one({"_id": ObjectId(category_id)}))


@app.route("/categories/delete/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    return redirect(url_for("get_categories"))


#About Page

@app.route('/about')
def about():
    """ About page with links, infor and social media"""
    return render_template("about.html")


# execute app__init__.py
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=(os.environ.get('PORT')), debug=True)
