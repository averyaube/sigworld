from flask import Flask, redirect, make_response
from flask.ext.pymongo import PyMongo
from random import random


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'sigs'
mongo = PyMongo(app)


@app.route('/link')
def random_url():
    link = mongo.db.links.find_one_or_404({"rand": {"$gte": random()}})
    return redirect(link['url'])


@app.route('/pic')
def random_pic():
    pic = mongo.db.pics.find_one_or_404({"rand": {"$lte": 0.4}})  # random()}})
    return make_response((pic['img'], 200, {'Content-Type': 'image/png'}))


if __name__ == '__main__':
    app.run(debug=True)
