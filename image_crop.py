import Image
import random
import pymongo
import bson
from StringIO import StringIO
import requests

# Do we care about configuration for this?
db = pymongo.Connection()
pics = db.sigs.pics
links = db.sigs.links


def store_section(content, size):
    """saves out a fucking section of an image file of the passed in image filename & dimensions"""
    image = Image.open(content)
    # gets the max coordinates we could be
    maxCoords = (image.size[0] - size[0], image.size[1] - size[1])
    # get random coordinates up to max
    randCoords = (random.randint(0, maxCoords[0]), random.randint(0, maxCoords[1]))
    # create cropped region
    region = (randCoords[0], randCoords[1], randCoords[0] + size[0], randCoords[1] + size[1])
    # create brand new image from region
    newImage = image.crop(region)
    # save out image
    buf = StringIO()
    newImage.save(buf, format="PNG")
    pics.insert({
        'rand': random.random(),
        'img': bson.binary.Binary(buf.getvalue())
    })


def process_image(url):
    """fukin takes an image url and turns it into a sig!!!"""
    r = requests.get(url)
    if r.status_code == 200:
        buff = StringIO(r.content)
        store_section(buff, (325, 60))
        return True
    else:
        return False


def insert_link(url):
    links.insert({
        'rand': random.random(),
        'url': url
    })
