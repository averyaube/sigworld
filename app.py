from flask import Flask, redirect, make_response
from flask.ext.pymongo import PyMongo
from random import random


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'sigs'
mongo = PyMongo(app)


@app.route('/link')
def random_url():
    order = 1 if random() > 0.5 else -1
    link = mongo.db.links.find_one_or_404({"rand": {"$gte": random()}}, sort=[('rand', order)])
    return redirect(link['url'])


@app.route('/pic')
def random_pic():
    order = 1 if random() > 0.5 else -1
    pic = mongo.db.pics.find_one_or_404({"rand": {"$gte": random()}}, sort=[('rand', order)])
    return make_response((pic['img'], 200, {'Content-Type': 'image/png'}))


if __name__ == '__main__':
    app.run(debug=True)
