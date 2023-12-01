from flask import Flask, render_template, request, redirect, url_for
from peewee import SqliteDatabase, Model, CharField

app = Flask(__name__)
db = SqliteDatabase('database.db')

class YourModel(Model):
    name = CharField()

db.connect()
db.create_tables([YourModel])

# Create operation
@app.route('/create', methods=['POST'])
def create():
    name = request.form.get('name')
    YourModel.create(name=name)
    return redirect(url_for('index'))

# Read operation
@app.route('/')
def index():
    data = YourModel.select()
    return render_template('index.html', data=data)

# Delete operation
@app.route('/delete/<int:id>')
def delete(id):
    YourModel.delete().where(YourModel.id == id).execute()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
