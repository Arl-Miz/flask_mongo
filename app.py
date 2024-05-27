from flask import Flask, render_template, request, url_for, redirect 
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

import urllib 

connection_string = f'mongodb+srv://arl:{urllib.parse.quote("Aliramezani72@")}@cluster.aiysjr7.mongodb.net/'

client = MongoClient(connection_string)

db = client.flask_database
todos = db.todos

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == "POST":   
        name = request.form['name']
        price = request.form['price']
        image = request.form.get['image']
        sell_unit = request.form['sell_unit']
        ret = request.form['ret']
        rating = request.form['rating']
        todos.insert_one({'name': name, 'price': price, 'image': image, 'sell_unit': sell_unit, 'ret': ret,  'rating': rating})
        return redirect(url_for('index')) 
    all_todos = todos.find()    
    return render_template('index.html', todos=all_todos) 

    


@app.route("/add-item", methods=('POST',))
def add_item():
    name = request.form['name']
    price = request.form['price']
    image = request.form['image']
    sell_unit = request.form['sell_unit']
    ret = request.form['ret']
    rating = request.form['rating']
    todos.insert_one({'name': name, 'price': price, 'image': image, 'sell_unit': sell_unit, 'ret': ret,  'rating': rating})
    return redirect(url_for('index'))

@app.route("/<id>/edit", methods=('POST',))
def edit_item(id):
    name = request.form['name']
    
    todos.update_one({'_id': ObjectId(id)}, {'$set': {'name': name}})
    return redirect(url_for('index'))

@app.post("/<id>/delete/")
def delete(id): 
    todos.delete_one({"_id": ObjectId(id)}) 
    return redirect(url_for('index')) 


if __name__ == "__main__":
    app.run(debug=True) 
