from flask import Flask, render_template, request, redirect, url_for
from peewee import SqliteDatabase, Model, CharField

app = Flask(__name__)
db = SqliteDatabase('database.db')

class YourModel(Model):
    name = CharField()

db.connect()
db.create_tables([YourModel])

# Your routes and CRUD operations here...

if __name__ == "__main__":
    app.run(debug=True)
