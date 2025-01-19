from flask import Flask, jsonify
import os
from config import Config
from uuid import uuid4

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.id = str(uuid4())
        self.name = name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }


@app.route("/")
def home():
    hname = os.uname().nodename
    return (f"Welcome to my app:V3 from {hname}\n")


@app.route("/create")
def create():
    user = User("test")
    print("new user", user)
    db.session.commit()

    return "done", 201


@app.route("/read")
def read():
    users = User.query.all()
    users = map(lambda x: x.serialize(), users)
    print(users)

    return jsonify(list(users)), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="localhost")
