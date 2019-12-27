import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipesDB'

# MONGODB_NAME = os.environ.get('MONGODB_NAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_users')
def get_users():
    return render_template("users.html", tasks=mongo.db.users.find())

# execute app__init__.py
if __name__ == '__main__':


    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
