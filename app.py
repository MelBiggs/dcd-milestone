import os
import urllib
import random
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
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)
# Enable text search for recipe names 
mongo.db.recipes.create_index([('name','text')])

# Home Page 
@app.route('/')
def home():
    """ Home page with recipe generator """
    recipes = ([recipe for recipe in mongo.db.recipes.aggregate([{"$sample": {"size": 1}}])])
    return render_template("index.html", recipe=recipes[0])


# Log in / Log Out / Register

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = mongo.db.users.find_one({"email": email})

        if (not user):
            flash('The login details are not correct')
            return render_template("login.html")

        if (not check_password_hash(user["password"], password)):
            flash('The login details are not correct')
            return render_template("login.html")

        session["user"] = user["username"]

        flash('Good to see you, ' + user["username"] + "!")
        return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/logout", methods=["GET"])
def logout():
    if(session.get('user')):
        session.pop("user")
    return redirect(url_for("home"))


@app.route('/register', methods=["GET", "POST"])
def register_user():
    # only allow users through if they are not logged in
    if not session.get('user'):

        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            repeat_password = request.form.get("repeat_password")
            email = request.form.get("email")
            dob = request.form.get("dob")

            errors=[]

            if (password != repeat_password):
                errors.append("Passwords do not match")

            if (not password or not username or not email or not dob):
                errors.append("All fields required")

            if (mongo.db.users.find_one({"username": username})):
                errors.append("Username is taken")
                
            if (mongo.db.users.find_one({"email": email})):
                errors.append("Existing email")

            if(len(errors) > 0):
                flash(errors)
                return render_template("registration.html", data=request.form.to_dict(), errors=errors)

            password = generate_password_hash(password)

            mongo.db.users.insert_one(
                {"username": username, "email": email, "password": password, "dob": dob})

            # Creates a cookie to store logged in user
            session["user"] = username

            return redirect(url_for("home"))
        return render_template("registration.html", data={})
    return redirect(url_for("home"))


# Recipes CRUD

# Create Recipe
@app.route('/recipes/create', methods=['GET', 'POST'])
def create_recipe():
    # User must be logged in to create a recipe 
    if session.get('user'):
        if request.method == "POST":

            data = request.form.to_dict()

            # Assign the logged in user to the new recipe
            data['user'] = session['user']

            data['slug'] = urllib.parse.quote_plus(data['slug'].replace(" ", "_"))

            if (mongo.db.recipes.find_one({"name": data['name']})):
                flash("Existing recipe")
                return render_template("create_recipes.html", recipe={})

            if (mongo.db.recipes.find_one({"slug": data['slug']})):
                flash("Existing slug")
                return render_template("create_recipes.html", recipe={})

            # Getting the list of ingredients and delete the incorrect data placeholder
            data.update({'ingredients': request.form.getlist('ingredients[]')})
            del data['ingredients[]']

            data.update({'steps': request.form.getlist('steps[]')})
            del data['steps[]']

            data['likes'] = []
            
            mongo.db.recipes.insert_one(data)
            return redirect(url_for("get_recipes"))
            
        categories = mongo.db.categories.find()
        return render_template("create_recipes.html", recipe={}, categories=categories)
    return redirect(url_for("login"))


# Read Recipes as Group, Individual, by Search

@app.route('/recipes', methods=['GET'])
def get_recipes():
    return render_template("recipes.html", current_category={},
        categories=mongo.db.categories.find(), 
        recipes=mongo.db.recipes.find())


@app.route('/recipes/<slug>', methods=['GET'])
def view_recipe(slug):
    return render_template("show_recipe.html",
        categories=mongo.db.categories.find(),
        recipe=mongo.db.recipes.find_one({"slug": slug})) 


@app.route('/search', methods=['POST'])
def search():
    results=mongo.db.recipes.find({"$text":{'$search': request.form.get("search_term")}})
    print(results)

    return render_template("results.html", results=results)


# Update / Edit Recipe

@app.route('/recipes/edit/<recipe_id>', methods=["GET", "POST"])
def edit_recipe(recipe_id):

    if(session.get('user')):
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

        # If a user tries to edit another users recipe, redirect them to the home page
        if recipe['user'] != session['user']:
            return redirect(url_for("home"))

        if request.method == "POST":

            recipes = mongo.db.recipes
            data = request.form.to_dict()
      
            # Assign the logged in user to the recipe
            data['user'] = session['user']
            print(data["slug"])

            # Make the slug url safe and replace spaces with underscores
            data['slug'] = urllib.parse.quote_plus(data['slug'].replace(" ", "_"))

            # If slug has been changed, make sure it is not already being used by another recipe
            if(data['slug'] != recipe['slug']):
                if (recipes.find_one({"slug": data['slug']})):
                    flash("This slug is taken")
                    return render_template("edit_recipes.html", recipe=data)

            # If name has been changed, make sure it is not already being used by another recipe
            if(data['name'] != recipe['name']):
                if (recipes.find_one({"name": data['name']})):
                    flash("This recipe name is taken")
                    return render_template("edit_recipes.html", recipe=data)

            data.update({'ingredients': request.form.getlist('ingredients[]')})
            del data['ingredients[]']

            data.update({'steps': request.form.getlist('steps[]')})
            del data['steps[]']

            data['likes'] = recipe['likes']

            mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, data)
            return redirect(url_for("get_recipes"))

        categories = mongo.db.categories.find()
        return render_template("edit_recipes.html", categories=categories, recipe=recipe)
    return redirect(url_for("login"))


# Delete Recipe 
@app.route("/recipes/delete/<recipe_id>", methods=['GET'])
def delete_recipe(recipe_id):
    if(session.get('user')):
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        if recipe['user'] != session['user']:
            return redirect(url_for("get_recipes"))
    
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})

    return redirect(url_for('get_recipes'))


# Like a Recipe
@app.route('/like/<recipe_id>', methods=['GET'])
def like_recipe(recipe_id):
    if session.get('user'):
        user = session.get('user')
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        # Gets list of likes for recipe
        likes = recipe['likes']
        # Check if user has already liked it, if so, remove the like. If not, add the like
        if(user in likes):
            likes.remove(user)
        else:
            likes.append(user)
        
        recipe['likes'] = likes
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, recipe)

    return redirect(url_for('view_recipe', slug=recipe['slug']))

# About Page

@app.route('/about')
def about():
    """ About page with links, infor and social media"""
    return render_template("about.html")


# User Profile 
# Get Profile 
@app.route('/users/<username>', methods=["GET"])
def user_profile(username):

    user = mongo.db.users.find_one({"username": username})

    return render_template("user_profile.html", 
        categories=mongo.db.categories.find(),
        user=user,
        recipes=mongo.db.recipes.find({"user": user['username']}))


# Edit Profile 
@app.route('/users/<username>/edit', methods=['GET', 'POST'])
def edit_profile(username):
    if(session.get('user')):
        user = mongo.db.users.find_one({"username": username})

        # If the logged in user is trying to edit a different user, send them to home page
        if user['username'] != session['user']:
            return redirect(url_for("home"))

        if request.method == "POST":
            data = request.form.to_dict()
            # If the current password is incorrect, give error 
            if (not check_password_hash(user["password"], data['current_password'])):
                return "incorrect current password details"
            # If repeated password doesn't match new password, give error
            if data['repeat_password'] != data['password']:
                return "passwords dont match"
            # Delete repeat password and old password from form data
            del data['repeat_password'] 
            del data['current_password']  
            # Add missing username and dob into data object
            data['dob'] = user['dob']
            data['username'] = user['username'] 
            # Replace form data for password with password hash
            data['password'] = generate_password_hash(data['password'])
            # Update database
            mongo.db.users.update({"_id": ObjectId(user['_id'])}, data)
            return redirect(url_for("user_profile", username=username))

        else:
            return render_template("edit_profile.html", user=user)
  
    return redirect(url_for('user_profile', username=username))


# Admin Only Pages - Users and Categories CRUD
@app.route('/get_users')
def get_users():
    if (session.get('user')):
        if session['user'] != 'Admin':
            return redirect(url_for('home'))
        return render_template("users.html", users=mongo.db.users.find())
    return redirect(url_for("login"))


@app.route('/categories/create', methods=["GET", "POST"])
def create_category():
    if (session.get('user')):
        if session['user'] != 'Admin':
            return redirect(url_for('home'))

        if request.method == "POST":
            name = request.form.get("name")

            if (mongo.db.categories.find_one({"name": name})):
                return "existing category"

            mongo.db.categories.insert_one({"name": name})
            return redirect(url_for("get_categories"))

        return render_template("create_categories.html", category={})
    return redirect(url_for("login"))


@app.route('/category/<category>')
def view_category(category):
    return render_template("recipes.html", current_category=category,
        categories=mongo.db.categories.find(), 
        recipes=mongo.db.recipes.find({"category_name": category}))


@app.route('/categories', methods=["GET"])
def get_categories():
    if (session.get('user')):
        if session['user'] != 'Admin':
            return redirect(url_for('home'))
        
        return render_template("categories.html", categories=mongo.db.categories.find())
    return redirect(url_for("login"))


@app.route('/categories/edit/<category_id>', methods=["GET", "POST"])
def edit_category(category_id):
    if (session.get('user')):
        if session['user'] != 'Admin':
            return redirect(url_for('home'))
        
        if request.method == "POST":
            name = request.form.get("name")

            if (mongo.db.categories.find_one({"name": name})):
                return "existing category"

            categories = mongo.db.categories
            categories.update({"_id": ObjectId(category_id)}, {"name": name})

            return redirect(url_for("get_categories"))

        return render_template("edit_categories.html", category=mongo.db.categories.find_one({"_id": ObjectId(category_id)}))
    return redirect(url_for("login"))


@app.route("/categories/delete/<category_id>")
def delete_category(category_id):
    if (session.get('user')):
        if session['user'] != 'Admin':
            return redirect(url_for('home'))

        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        return redirect(url_for("get_categories"))
    return redirect(url_for("login"))


# execute app__init__.py
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=(os.environ.get('PORT')), debug=False)
